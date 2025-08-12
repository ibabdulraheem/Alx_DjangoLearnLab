from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from blog import views as user_views



urlpatterns = [

path('register/', user_views.register.as_view(template_name = 'blog/register.html'),name='register'),
path('login/',auth_views.LoginView.as_view(template_name = 'blog/login.html'),name = 'login'),
path('login/',auth_views.LogoutView.as_view(template_name = 'blog/logout.html'),name = 'logout'),
path('profile/')
]