from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category
from post.models import Post


def OK(request, **kwargs):
    return render(request, 'OK_user')


class PostsByCategory(DetailView):
    template_name = 'category/posts-by-category.html'
    context_object_name = 'category'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(PostsByCategory, self).get_context_data()
        context['posts_list'] = Post.posts.get_queryset_by_category(self.kwargs['pk'])
        return context

