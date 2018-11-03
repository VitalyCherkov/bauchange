from django.urls import path
from . import views

app_name = 'category'
urlpatterns = [
    path('<int:pk>/', views.PostsByCategory.as_view(), name='posts-by-category'),
    path('', views.AllCategories.as_view(), name='all-categories'),
]