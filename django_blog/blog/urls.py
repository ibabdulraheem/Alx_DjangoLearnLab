from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from blog import views as user_views
from . import views
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

# templates for listing, viewing, creating, editing, and deleting blog posts.

urlpattern = [
path('register/', user_views.register.as_view(template_name = 'blog/register.html'),name='register'),
path('login/',auth_views.LoginView.as_view(template_name = 'blog/login.html'),name = 'login'),
path('login/',auth_views.LogoutView.as_view(template_name = 'blog/logout.html'),name = 'logout'),
path('profile/'),
path('', views.post_list(template_name='blog/post_list.html'), name='post_list'), #list all post
path('post/new/', views.create_post(template_name='blog/post_form.html'), name='create_post'),  # create new post
path('post/<int:pk>/', views.post_detail(template_name='blog/post_detail.html'), name='post_detail'), # view single post
path('post/<int:pk>/update/', views.update_post(template_name='blog/post_form.html'), name='update_post'), # Edit existing post
path('post/<int:pk>/delete/', views.delete_post(template_name='blog/post_form_delete.html'), name='delete_post'), # Delete a post
path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment_create'),
path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
path('search/', views.post_search, name='post_search'),
]

# ["comment/<int:pk>/update/", "post/<int:pk>/comments/new/", "comment/<int:pk>/delete/"]