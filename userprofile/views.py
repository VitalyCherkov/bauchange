from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from .models import UserProfile

class UserPage(DetailView):
    model = UserProfile
    template_name = 'userprofile/userpage.html'
    context_object_name = 'userprofile'

    def get_context_data(self, **kwargs):





class SignUpView(LoginView):

    form_class = SignUpForm
    template_name = 'userprofile/singup.html'
    redirect_authenticated_user = True