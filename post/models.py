from django.db import models
from category.models import Category
from tag.models import Tag
from user.models import User


class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset()

    def get_queryset_by_user(self, user):
        return self.get_queryset().filter(user=user)

    def get_queryset_by_category(self, category):
        return self.get_queryset().filter(category=category)

    def get_queryset_by_tag(self, tag):
        return self.get_queryset().filter(tag=tag)

    def get_queryset_mixed(self, **kwargs):
        queryset = self.get_queryset()

        if 'user' in kwargs:
            queryset.filter(user=kwargs['user'])

        if 'tag' in kwargs:
            queryset.filter(tag=kwargs['tag'])

        if 'category' in kwargs:
            queryset.filter(category=kwargs['category'])

        return queryset


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    posts = PostManager()

    def __str__(self):
        return '#{0}: {1}'.format(self.id, self.title)
