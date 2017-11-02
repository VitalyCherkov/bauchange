from django.db import models
#from post.models import Post
from user.models import User


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    is_the_best = models.BooleanField(default=False)
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}: {1}...".format(self.pub_date, self.text[:50])
