from django.conf.urls import url
from . import views

app_name = 'userprofile'
urlpatterns = [
    url(r'^(?P<pk>\d+)/', views.OK, name='userprofile-page'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]