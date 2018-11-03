from django.conf.urls import url
from django.urls import path
from . import views
from .api.viewsets import PostViewSet

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
})

post_vote = PostViewSet.as_view({
    'post': 'vote',
})

app_name = 'post'
urlpatterns = [
    path('create/', views.CreatePost.as_view(), name='create'),
    path('<int:pk>/vote', post_vote, name='post-vote'),
    path('<int:pk>/', views.DetailPost.as_view(), name='detail'),
    path('hot/', views.PopularPosts.as_view(), name='popular'),
    path('api/<int:pk>/', post_detail, name='api-detail'),
    path('', views.ListPost.as_view(), name='list'),
]