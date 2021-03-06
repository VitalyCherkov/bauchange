from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from bauchange import settings
from .models import Post
from .forms import CreatePostForm
from comment.models import Comment
from comment.views import CommentsList


class DetailPost(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        self.object.take_a_view()
        context = super(DetailPost, self).get_context_data()

        vote = self.object.voted_by_cur(user=self.request.user)
        if vote == settings.LIKE:
            context['is_liked'] = 'active'
        elif vote == settings.DISLIKE:
            context['is_disliked'] = 'active'

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


class PopularPosts(ListPost):
    def get_queryset(self):
        return self.model.posts.get_popular()


class CreatePost(LoginRequiredMixin, CreateView):
    template_name = 'post/create.html'
    form_class = CreatePostForm

    def form_valid(self, form):
        form.set_user(self.request.user)
        return super(CreatePost, self).form_valid(form)
