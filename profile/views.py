from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import User


def OK(request, **kwargs):
    return render(request, 'profile/settings.html')

#class UserProfile(DetailView):
#    template_name = 'profile/settings.html'
#    model = User

