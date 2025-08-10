from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import UserLoginView,UserLogoutView,BookListView

urlpatterns = [
  path ('list_books/',views.list_books(template_name= list_books.html), name ='list_books'),
  path ('books_by_library/',views.BookListView.as_view(), name = 'book_by_library'),
  path('login/',views.UserLoginView.as_view(template_name="login/login.html"), name="login"),
  path ('logout/',views.UserLogoutView.as_view(template_name="logout/logout.html"), name="logout"),
  path ('register/',views.SignUpView.as_view(template_name="register/register.html"), name="register"),
]
