from django.shortcuts import reverse, get_object_or_404
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    about = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('userprofile:userpage', kwargs={'pk': self.pk})

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

    def get_current_userprofile(user):
        return get_object_or_404(UserProfile, user=user)