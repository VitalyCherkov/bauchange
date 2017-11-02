from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    rating = models.IntegerField(default=0)
    password = models.CharField(max_length=30)

    def __str__(self):
        return '#{0}: {1}'.format(self.id, self.name)