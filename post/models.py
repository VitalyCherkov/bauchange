from django.core.urlresolvers import reverse
from django.db import models
from category.models import Category
from tag.models import Tag
from user.models import User


class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset()

    def get_popular(self):
        return self.get_queryset().order_by('-likes')

    def get_queryset_by_user(self, user):
        return self.get_queryset().filter(user=user)

    def get_queryset_by_category(self, category):
        return self.get_queryset().filter(category=category)

    def get_queryset_by_tag(self, tag):
        return self.get_queryset().filter(tag=tag)


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    posts = PostManager()

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '#{0}: {1}'.format(self.id, self.title)
