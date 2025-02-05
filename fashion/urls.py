from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('', views.PostListView, name='home'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/articles/', views.article_list, name='article_list'),
    path('posts/', views.PostListView, name='post_list'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('fashion/', views.fashion, name='fashion'),
]