from django.core.urlresolvers import reverse
from django.db import models
from category.models import Category
from tag.models import Tag
from userprofile.models import UserProfile


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
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)

    deleted = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)

    posts = PostManager()

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})

    def take_a_view(self):
        self.views += 1
        self.save()
        return self.views

    def __str__(self):
        return '#{0}: {1}'.format(self.id, self.title)
