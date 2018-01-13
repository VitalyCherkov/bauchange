from django.views.generic.detail import DetailView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from .forms import SignUpForm
from .forms import EditProfileForm
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


class EditView(UserPassesTestMixin, UpdateView):

    model = UserProfile
    template_name = 'userprofile/settings.html'
    form_class = EditProfileForm
    redirect_field_name = None

    def get_form(self, form_class=None):
        form = super(EditView, self).get_form()
        form.update_initial()
        return form

    def test_func(self):

        editing_user = get_object_or_404(UserProfile, pk=self.kwargs['pk']).user
        return self.request.user.is_authenticated and self.request.user == editing_user
