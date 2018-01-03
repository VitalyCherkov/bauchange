from django.db import models
from post.models import Post
from userprofile.models import UserProfile


class CommentManager(models.Manager):
    def get_queryset(self, author):
        if author is None:
            return super(CommentManager, self).get_queryset()

        return super(CommentManager, self).get_queryset().filter(author=author)


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
