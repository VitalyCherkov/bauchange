from django.db import models
from category.models import Category
from tag.models import Tag
from user.models import User


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

    def __str__(self):
        return '#{0}: {1}'.format(self.id, self.title)
