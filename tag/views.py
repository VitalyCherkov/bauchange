from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.detail import DetailView
from .models import Tag
from post.models import Post
from post.views import ListPost


class PostsByTag(SingleObjectMixin, ListView):
    model = Tag
    template_name = "tag/posts-by-tag.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Tag.objects.all())
        return super(PostsByTag, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostsByTag, self).get_context_data(**kwargs)
        context['pag_options'] = ListPost.set_paginator_options(context)
        context['tag_label'] = self.object.label
        return context

    def get_queryset(self):
        return Post.posts.get_queryset_by_tag(self.object.pk)



class PopularTags(ListView):
    model = Tag
    context_object_name = 'tags'
    # template_name
