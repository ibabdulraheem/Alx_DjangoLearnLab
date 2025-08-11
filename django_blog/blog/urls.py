from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from blog import views as user_views



urlpatterns = [

path('register/', user_views.register, name='register'),
path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name = 'login'),
path('login/',auth_views.LogoutView.as_view(next_page = '/'),name = 'logout'),
]