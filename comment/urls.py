from django.conf.urls import url
from . import views
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
    url(r'^post/create/$', comment_create, name='comment-create'),
    url(r'^(?P<pk>\d+)/vote/$', comment_vote, name='comment-vote'),
    url(r'^$', comments_list, name='comments-list'),
]