from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'userprofile'
urlpatterns = [
    path('edit/<int:pk>/', views.EditView.as_view(), name='editprofile'),
    path('<int:pk>/', views.UserPageDetail.as_view(), name='userpage'),
    path('login/',
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='userprofile/login.html'),
        name='login'
        ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup')
]