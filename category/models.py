from django.db import models
from django.urls import reverse


class Category(models.Model):
    label = models.CharField(unique=True, max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.label

    def get_url(self):
        return reverse('category:posts-by-category', kwargs={'pk': self.pk})
