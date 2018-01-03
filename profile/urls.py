from django.conf.urls import url
from . import views

app_name = 'profile'
urlpatterns = [
    url(r'^(?P<pk>\d+)/', views.OK, name='profile-page'),
    # url(r'^settings/', views.)
]