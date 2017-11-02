from django.conf.urls import url
from . import views

app_name = 'tag'
urlpatterns = [
    url(r'^(?P<pk>\d+)/', views.OK, name='tag-posts'),
]