from django.db import models
from django.shortcuts import get_object_or_404
from post.models import Post
from userprofile.models import UserProfile


class CommentManager(models.Manager):

    def get_queryset(self):
        return super(CommentManager, self).get_queryset()

    def get_comments_by_post(self, post):
        if post is None:
            return self.get_queryset()

        return self.get_queryset().filter(post=post)

    def get_the_best_by_post(self, post):
        return get_object_or_404(Comment, post=post, is_the_best=True)

    def get_comments_by_author(self, author):
        if author is None:
            return self.get_queryset()
        print(author)
        return self.get_queryset().filter(author=author)


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    is_the_best = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, blank=True, on_delete=models.CASCADE)

    comments = models.Manager()
    author_comments = CommentManager()

    def __str__(self):
        return "{0}: {1}...".format(self.pub_date, self.text[:50])
