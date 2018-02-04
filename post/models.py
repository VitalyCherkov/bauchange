from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from category.models import Category
from tag.models import Tag
from userprofile.models import UserProfile
from bauchange import settings
from . import model_managers


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

    def __str__(self):
        action = 'LIKE   ' if self.action is settings.LIKE else 'DISLIKE'

        return '{0}_{1}   {2}   {3}'.format(
            self.content_type,
            self.object_id,
            action,
            self.user_profile
        )

    objects = model_managers.VotesManager()


def do_vote_base(obj, user_profile, action):
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


class Post(models.Model):

    class Meta:
        ordering = ['-pub_date']

    title = models.CharField(max_length=250)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = GenericRelation(Vote, related_query_name='posts')

    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, related_name='own_posts')

    deleted = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)

    posts = model_managers.PostManager()

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})

    def take_a_view(self):
        self.views += 1
        self.save()
        return self.views

    def voted_by_cur(self, user):

        if user.is_authenticated:
            cur_user = user.user_profile
        else:
            cur_user = None

        try:
            content_type = ContentType.objects.get_for_model(self)
            vote = Vote.objects.get(user_profile=cur_user, content_type=content_type, object_id=self.pk)
            vote = vote.action
        except Vote.DoesNotExist:
            vote = None

        return vote

    def do_vote(self, user_profile, action):
        return do_vote_base(obj=self, user_profile=user_profile, action=action)

    def get_vote_url(self):
        return reverse('post:post-vote', kwargs={'pk': self.pk})

    def get_api_url(self):
        return reverse('post:api-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '#{0}: {1}'.format(self.id, self.title)













