from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
from .models import Category
from post.models import Post
from post.views import ListPost


def OK(request, **kwargs):
    return render(request, 'OK_user')


"""
class PostsByCategory(DetailView):
    template_name = 'category/posts-by-category.html'
    context_object_name = 'category'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(PostsByCategory, self).get_context_data()
        context['posts_list'] = Post.posts.get_queryset_by_category(self.kwargs['pk'])
        return context
"""


class PostsByCategory(SingleObjectMixin, ListView):
    model = Category
    template_name = "category/posts-by-category.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super(PostsByCategory, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostsByCategory, self).get_context_data(**kwargs)
        context['pag_options'] = ListPost.set_paginator_options(context)
        context['category_label'] = self.object.label
        return context

    def get_queryset(self):
        return Post.posts.get_queryset_by_category(self.object.pk)