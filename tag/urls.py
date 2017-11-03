from django.conf.urls import url
from . import views
from .views import PostsByTag

app_name = 'tag'
urlpatterns = [
    url(r'^(?P<pk>\d+)/', PostsByTag.as_view(), name='posts-by-tag'),
    #url(r'^$', )
]