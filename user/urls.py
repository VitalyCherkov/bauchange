from django.conf.urls import url
from . import views

app_name = 'user'
urlpatterns = [
    url(r'^(?P<pk>\d+)/', views.OK, name='user-page'),
    # url(r'^settings/', views.)
]