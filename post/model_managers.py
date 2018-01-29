from django.db import models
from bauchange import settings

class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset()

    def get_popular(self):
        return self.get_queryset().order_by('-views')

    def get_queryset_by_author(self, author):
        return self.get_queryset().filter(author=author)

    def get_queryset_by_category(self, category):
        return self.get_queryset().filter(category=category)

    def get_queryset_by_tag(self, tag):
        return self.get_queryset().filter(tag=tag)


class VotesManager(models.Manager):
    use_for_related_fields = True

    def get_likes(self):
        return self.get_queryset().filter(action=settings.LIKE).count()

    def get_dislikes(self):
        return self.get_queryset().filter(action=settings.DISLIKE).count()

    def get_total(self):
        return self.get_likes() - self.get_dislikes()
