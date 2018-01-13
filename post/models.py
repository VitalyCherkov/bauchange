from django.core.urlresolvers import reverse
from django.db import models
from category.models import Category
from tag.models import Tag
from userprofile.models import UserProfile
from django.utils.translation import ugettext_lazy as _


class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset()

    def get_popular(self):
        return self.get_queryset().order_by('-likes')

    def get_queryset_by_author(self, author):
        return self.get_queryset().filter(author=author)

    def get_queryset_by_category(self, category):
        return self.get_queryset().filter(category=category)

    def get_queryset_by_tag(self, tag):
        return self.get_queryset().filter(tag=tag)


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

    posts = PostManager()

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})

    def get_likes(self):
        return

    def take_a_view(self):
        self.views += 1
        self.save()
        return self.views

    def __str__(self):
        return '#{0}: {1}'.format(self.id, self.title)


class LikeDislikeManager(models.Manager):
    def get_queryset(self):
        return super(LikeDislikeManager, self).get_queryset()

    def get_likes(self):
        return self.get_queryset().filter(vote=LikeDislike.LIKE)

    def get_dislikes(self):
        return self.get_queryset().filter(vote=LikeDislike.DISLIKE)

    def get_likes_by_post(self, post):
        return self.get_likes().filter(post__pk=post.pk)

    def get_dislikes_by_post(self, post):
        return self.get_dislikes().filter(post__pk=post.pk)

    def get_likes_by_user(self, user_profile):
        return self.get_likes().filter(user_profile__pk=user_profile.pk)

    def get_dislikes_by_user(self, user_profile):
        return self.get_dislikes().filter(user_profile__pk=user_profile.pk)


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Dislike'),
        (LIKE, 'Like')
    )

    vote = models.SmallIntegerField(choices=VOTES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        value = 'like' if self.vote == self.LIKE else 'dislike'
        return 'Post_{0} -{1}- User_{2}'.format(self.post.pk, value, self.user_profile.pk)

    likes_dislikes = LikeDislikeManager()






