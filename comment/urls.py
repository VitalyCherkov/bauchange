from django.conf.urls import url
from . import views


app_name = 'comments'
urlpatterns = [
    url(r'^post/(\d+)$', views.CommentsList.as_view(), name='post-comments'),
]