from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Comment


class CommentsList(ListView):
    model = Comment
    template_name = 'comment/list.html'
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):
        context = super(CommentsList, self).get_context_data()
        context['comments'] = Comment.user_comments.get_queryset(self.args[0])

        for comment in context['comments']:
            print(comment)

        return context
