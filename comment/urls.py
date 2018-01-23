from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views
from .api.viewsets import CommentViewSet


comments_list = CommentViewSet.as_view({
    'post': 'create',
    'get': 'retrieve'
})


app_name = 'comments'
urlpatterns = [
    url(r'^post/(\d+)$', views.CommentsList.as_view(), name='post-comments'),
    url(r'^post/comments/$', comments_list, name='comment-create')
]