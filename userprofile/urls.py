from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'userprofile'
urlpatterns = [
    url(r'^(?P<pk>\d+)/', views.UserPage.as_view(), name='userpage'),
    url(r'^login/$',
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='userprofile/login.html'),
        name='login'
        ),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup')
]