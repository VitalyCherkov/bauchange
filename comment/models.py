from django.db import models
from django.shortcuts import get_object_or_404, reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from post.models import Post, Vote, do_vote_base as _do_vote
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
    is_the_best = models.BooleanField(default=False)

    rating = GenericRelation(Vote, related_query_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, blank=True, on_delete=models.CASCADE)

    comments = models.Manager()
    author_comments = CommentManager()

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return "{0}: {1}...".format(self.pub_date, self.text[:50])

    def get_vote_url(self):
        return reverse('comments:comment-vote', kwargs={'pk': self.pk})

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
        return _do_vote(obj=self, user_profile=user_profile, action=action)




