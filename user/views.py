from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import User


def OK(request, **kwargs):
    return render(request, 'user/settings.html')

#class UserProfile(DetailView):
#    template_name = 'user/settings.html'
#    model = User

