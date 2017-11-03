from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post
from comment.models import Comment
from comment.views import CommentsList


def create(request):
    return render(request, 'post/create.html', {})


class DetailPost(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(DetailPost, self).get_context_data()
        context[CommentsList.context_object_name] = Comment.user_comments.get_queryset(self.kwargs['pk'])
        return context


class ListPost(ListView):
    model = Post
