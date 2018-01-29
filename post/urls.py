from django.conf.urls import url
from . import views
from .api.viewsets import PostViewSet



post_vote = PostViewSet.as_view({
    'post': 'vote',
})

app_name = 'post'
urlpatterns = [
    url(r'^create/$', views.CreatePost.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/vote/$', post_vote, name='post-vote'),
    url(r'^(?P<pk>\d+)/$', views.DetailPost.as_view(), name='detail'),
    url(r'^hot/$', views.PopularPosts.as_view(), name='popular'),
    url(r'^$', views.ListPost.as_view(), name='list'),
]