from django.conf.urls import url
from django.urls import path
from .api.viewsets import CommentViewSet

comments_list = CommentViewSet.as_view({
    'get': 'list'
})

comment_create = CommentViewSet.as_view({
    'post': 'create',
    'get': 'retrieve',
})

comment_vote = CommentViewSet.as_view({
    'post': 'vote'
})

app_name = 'comments'
urlpatterns = [
    path('post/create', comment_create, name='comment-create'),
    path('<int:pk>/vote/', comment_vote, name='comment-vote'),
    path('', comments_list, name='comments-list'),
]