from django.shortcuts import render
from django.urls import reverse

from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView

from django.conf import settings


def OK(request, **kwargs):
    return render(request, 'userprofile/settings.html')


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'userprofile/login.html'
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):

    url = settings.LOGOUT_REDIRECT_URL

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).get(request, args, kwargs)
