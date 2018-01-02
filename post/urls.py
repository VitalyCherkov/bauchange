from django.conf.urls import url
from . import views


app_name = 'post'
urlpatterns = [
    url(r'^create/$', views.CreatePost.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/', views.DetailPost.as_view(), name='detail'),
    url(r'^$', views.ListPost.as_view(), name='list'),
    url(r'^hot/$', views.ListPost.as_view(), name='list'),
]