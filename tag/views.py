from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tag
from post.models import Post

def OK(request, **kwargs):
    return render(request, 'OK_user')


class PostsByTag(DetailView):
    model = Tag
    context_object_name = 'tag'
    template_name = 'tag/posts-by-tag.html'

    def get_context_data(self, **kwargs):
        context = super(PostsByTag, self).get_context_data()
        context['posts_list'] = Post.posts.get_queryset_by_tag(self.kwargs['pk'])
        return context


class PopularTags(ListView):
    model = Tag
    context_object_name = 'tags'
    # template_name
