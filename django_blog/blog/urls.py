from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from blog import views as user_views
from . import views



urlpatterns = [

path('register/', user_views.register.as_view(template_name = 'blog/register.html'),name='register'),
path('login/',auth_views.LoginView.as_view(template_name = 'blog/login.html'),name = 'login'),
path('login/',auth_views.LogoutView.as_view(template_name = 'blog/logout.html'),name = 'logout'),
path('profile/')
path('', views.post_list, name='post_list'), #list all post
path('post/new/', views.create_post, name='create_post'),  # create new post
path('post/<int:pk>/', views.post_detail, name='post_detail'), # view single post
path('post/<int:pk>/update/', views.update_post, name='update_post'), # Edit existing post
path('post/<int:pk>/delete/', views.delete_post, name='delete_post'), # Delete a post
]