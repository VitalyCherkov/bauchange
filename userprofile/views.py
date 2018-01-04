from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm

def OK(request, **kwargs):
    return render(request, 'userprofile/settings.html')


class SignUpView(LoginView):

    form_class = SignUpForm
    template_name = 'userprofile/singup.html'
    redirect_authenticated_user = True