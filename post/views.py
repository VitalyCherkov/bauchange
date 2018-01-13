import json
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Post, LikeDislike
from .forms import CreatePostForm
from userprofile.models import UserProfile
from comment.models import Comment
from comment.views import CommentsList


class DetailPost(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        self.object.take_a_view()
        context = super(DetailPost, self).get_context_data()
        context[CommentsList.context_object_name] = \
            Comment.author_comments.get_queryset(self.kwargs['pk'])

        context['likes'] = len(LikeDislike.likes_dislikes.get_likes_by_post(self.object))
        context['dislikes'] = len(LikeDislike.likes_dislikes.get_dislikes_by_post(self.object))

        return context


class ListPost(ListView):
    model = Post
    template_name = 'post/all-posts.html'
    context_object_name = 'posts_list'
    paginate_by = 10

    def set_paginator_options(context):
        first_index = max(context['page_obj'].number - 2, 1)
        last_index = min(first_index + 4, context['paginator'].num_pages)
        first_index = max(1, last_index - 4)

        return {
            'first': first_index,
            'last': last_index
        }

    def get_context_data(self, **kwargs):
        context = super(ListPost, self).get_context_data(**kwargs)
        context['pag_options'] = ListPost.set_paginator_options(context)
        return context


class CreatePost(LoginRequiredMixin, CreateView):
    template_name = 'post/create.html'
    form_class = CreatePostForm

    def form_valid(self, form):
        form.set_user(self.request.user)
        return super(CreatePost, self).form_valid(form)


class VoteViewAJAX(View):
    vote_type = None

    def post(self, request, pk):

        print(request, '\n\n', pk)

        result = None
        cur_post = Post.posts.get(pk=pk)
        print('user', request.user, '\n\n\n')
        cur_user_profile = UserProfile.objects.get(user=request.user)
        print(cur_post)

        try:
            print('kek')
            like_dislike = LikeDislike.likes_dislikes.get(
                post=cur_post,
                user_profile=cur_user_profile
            )
            print('kek')
            if like_dislike.vote != self.vote_type:
                like_dislike.vote = self.vote_type
                like_dislike.save()
                result = True
            else:
                like_dislike.delete()
                result = False

        except LikeDislike.DoesNotExist:
            print('try')
            like_dislike = LikeDislike(
                user_profile=cur_user_profile,
                post=cur_post,
                vote=self.vote_type
            )
            print('catch')
            like_dislike.save()
            result = True

        likes_count = len(cur_post.like_dislike.all().filter(likedislike__vote=LikeDislike.LIKE))
        dislikes_count = len(cur_post.like_dislike.all().filter(likedislike__vote=LikeDislike.DISLIKE))
        print('likes_count: ', likes_count)
        print('dislikes_count: ', dislikes_count)

        return HttpResponse(

            json.dumps({
                'result': result,
                'likes_count': likes_count,
                'dislikes_count': dislikes_count
            }),
            content_type='application/json'
        )


"""
    Проверить наличие
        Если есть
            Узнать тип
            Удалить
            Если типы не совпадают
                Создать
        Иначе
            Создать
"""





