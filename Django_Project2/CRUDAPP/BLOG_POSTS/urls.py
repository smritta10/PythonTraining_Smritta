from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts_list, name= 'Blog_list'),
    path('view/<int:pk>', views.blog_posts_view, name='blog_view'),
    path('new', views.blog_posts_create, name='blognew'),
    path('edit/<int:pk>', views.blog_posts_update, name='blog_edit'),
    path('delete/<int:pk>', views.blog_posts_delete, name='blog_delete'),
    ]