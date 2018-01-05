from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from .models import UserProfile
from post.models import Post
from post.views import ListPost

class UserPageDetail(SingleObjectMixin, ListView):
    model = UserProfile
    template_name = 'userprofile/userpage.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=UserProfile.objects.all())
        return super(UserPageDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserPageDetail, self).get_context_data(**kwargs)
        context['pag_options'] = ListPost.set_paginator_options(context)
        context['userprofile'] = self.object
        return context

    def get_queryset(self):
        return Post.posts.get_queryset_by_author(self.object.pk)



class UserPage(DetailView):
    model = UserProfile
    template_name = 'userprofile/userpage.html'
    context_object_name = 'userprofile'

    def get_context_data(self, **kwargs):
        context = super(UserPage, self).get_context_data()
        return context




class SignUpView(LoginView):

    form_class = SignUpForm
    template_name = 'userprofile/singup.html'
    redirect_authenticated_user = True