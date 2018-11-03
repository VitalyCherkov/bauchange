from django.urls import path
from .views import PostsByTag

app_name = 'tag'
urlpatterns = [
    path('<int:pk>/', PostsByTag.as_view(), name='posts-by-tag'),
]