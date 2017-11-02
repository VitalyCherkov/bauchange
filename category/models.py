from django.db import models


class Category(models.Model):
    label = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.label
