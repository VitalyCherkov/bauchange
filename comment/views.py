from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Comment


class CommentsList(ListView):
    model = Comment
    template_name = 'comment/list.html'

    def get_queryset(self):
        queryset = 

    def get_context_data(self, **kwargs):
        context = super(CommentsList, self).get_context_data(kwargs)
        context['comments'] = Comment.objects.filter(post=kwargs['pk'])
        return context
