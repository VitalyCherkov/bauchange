from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/(?P<pk>\d+)$', views.CommentsList.as_view, name='pagename'),
]