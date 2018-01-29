from django.conf.urls import url
from . import views
from .api.viewsets import CommentViewSet


comments_list = CommentViewSet.as_view({
    'post': 'create',
    'get': 'retrieve'
})

comment_vote = CommentViewSet.as_view({
    'post': 'vote'
})

app_name = 'comments'
urlpatterns = [
    url(r'^post/(\d+)$', views.CommentsList.as_view(), name='post-comments'),
    url(r'^post/comments/$', comments_list, name='comment-create'),
    url(r'^(?P<pk>\d+)/vote/$', comment_vote, name='comment-vote')
]