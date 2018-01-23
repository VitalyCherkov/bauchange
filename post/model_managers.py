from django.db import models
from bauchange import settings

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


class LikeDislikeManager(models.Manager):
    def get_queryset(self):
        return super(LikeDislikeManager, self).get_queryset()

    def get_likes(self):
        return self.get_queryset().filter(vote=settings.LIKE)

    def get_dislikes(self):
        return self.get_queryset().filter(vote=settings.DISLIKE)

    def get_likes_by_post(self, post):
        return self.get_likes().filter(post__pk=post.pk)

    def get_dislikes_by_post(self, post):
        return self.get_dislikes().filter(post__pk=post.pk)

    def get_likes_by_user(self, user_profile):
        return self.get_likes().filter(user_profile__pk=user_profile.pk)

    def get_dislikes_by_user(self, user_profile):
        return self.get_dislikes().filter(user_profile__pk=user_profile.pk)


class VotesManager(models.Manager):
    use_for_related_fields = True

    def get_likes(self):
        return self.get_queryset().filter(action=settings.LIKE)

    def get_dislikes(self):
        return self.get_queryset().filter(action=settings.DISLIKE)

    def get_total(self):
        print('BIG KEK')
        return self.get_likes().count() - self.get_dislikes().count()
