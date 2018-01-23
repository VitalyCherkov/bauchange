from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from category.models import Category
from tag.models import Tag
from userprofile.models import UserProfile
from bauchange import settings
from . import model_managers


class Post(models.Model):

    class Meta:
        ordering = ['-pub_date']

    title = models.CharField(max_length=250)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    like_dislike = models.ManyToManyField(UserProfile, through='LikeDislike')

    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, related_name='own_posts')

    deleted = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)

    posts = model_managers.PostManager()

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})

    def get_likes_count(self):
        return len(self.like_dislike.all().filter(likedislike__vote=settings.LIKE))

    def get_dislikes_count(self):
        return len(self.like_dislike.all().filter(likedislike__vote=settings.DISLIKE))

    def voted_by_cur(self, user):

        if user.is_authenticated:
            cur_user = UserProfile.get_current_userprofile(user)
        else:
            cur_user = None

        try:
            vote = LikeDislike.likes_dislikes.get(user_profile=cur_user, post=self)
            vote = 'like' if vote.vote == settings.LIKE else 'dislike'
        except LikeDislike.DoesNotExist:
            vote = None

        return vote

    def take_a_view(self):
        self.views += 1
        self.save()
        return self.views

    def __str__(self):
        return '#{0}: {1}'.format(self.id, self.title)


class LikeDislike(models.Model):
    VOTES = (
        (settings.DISLIKE, 'Dislike'),
        (settings.LIKE, 'Like')
    )

    vote = models.SmallIntegerField(choices=VOTES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        value = 'like' if self.vote == settings.LIKE else 'dislike'
        return 'Post_{0} -{1}- User_{2}'.format(self.post.pk, value, self.user_profile.pk)

    likes_dislikes = model_managers.LikeDislikeManager()


class Vote(models.Model):
    VOTES = (
        (settings.LIKE, 'Like'),
        (settings.DISLIKE, 'Dislike')
    )

    action = models.SmallIntegerField(choices=VOTES)
    user_profile = models.ForeignKey(UserProfile, verbose_name=_('Пользователь'))

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = model_managers.VotesManager()


def do_vote(obj, user_profile, action):
    try:
        vote = Vote.objects.get(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.id,
            user_profile=user_profile
        )
        if vote.action is not int(action):
            vote.action = action
            vote.save()
            return action
        else:
            vote.delete()
            return None

    except Vote.DoesNotExist:
        obj.rating.create(user_profile=user_profile, action=action)
        return action






