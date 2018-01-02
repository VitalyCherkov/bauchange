from django.conf.urls import include, url
from . import views

app_name = 'category'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.PostsByCategory.as_view(), name='posts-by-category'),
    url(r'^$', views.AllCategories.as_view(), name='all-categories'),
]