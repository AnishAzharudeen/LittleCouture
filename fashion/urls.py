from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/articles/', views.article_list, name='article_list'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
]