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
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('event/', views.event_list, name='event_list'),  
    path('event/<slug:slug>/', views.event_detail, name='event_detail'),
]