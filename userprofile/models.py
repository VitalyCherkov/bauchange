from django.shortcuts import reverse, get_object_or_404
from django.db import models
from django.contrib.auth.models import User
import uuid


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'avatar/%s/%s/%s' % (filename[:1], filename[2:3], filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    rating = models.IntegerField(default=0)
    about = models.TextField(blank=True)

    avatar = models.ImageField(upload_to=get_file_path, blank=True, null=True)

    def get_avatar_url(self):
        try:
            return self.avatar.url
        except Exception:
            return '/static/img/user_empty.png'

    def get_absolute_url(self):
        return reverse('userprofile:userpage', kwargs={'pk': self.pk})

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

    def get_current_userprofile(user):
        return get_object_or_404(UserProfile, user=user)