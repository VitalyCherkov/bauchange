from django.conf.urls import include, url
from . import views

app_name = 'category'
urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.OK, name='category-posts'),
]