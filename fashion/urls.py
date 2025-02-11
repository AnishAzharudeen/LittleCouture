from django.urls import path
from . import views
from .views import PostListView,like_article, create_article

urlpatterns = [

    path('', views.PostListView1.as_view(), name='home'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/articles/', views.article_list, name='article_list'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('fashion/', views.fashion, name='fashion'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('post/<slug:slug>/like/', views.like_article, name='like_article'),
    path('post/<slug:slug>/edit/', views.edit_article, name='edit_article'),
    path('post/<slug:slug>/delete/', views.delete_article, name='delete_article'),
    path('event/', views.event, name='event'),
    path('create_article/', views.create_article, name='create_article'),

]
