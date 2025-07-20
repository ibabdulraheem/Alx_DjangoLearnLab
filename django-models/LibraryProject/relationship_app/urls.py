from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
  path ('list_books/',views.list_books, name ='book_list'),
  path ('books_by_library/',views.BookListView.as_view(), name = 'book_by_library'),
  path('login/',LoginView.as_view(template_name = 'relationship_app/login.html'), name = 'login'),
  path ('logout/',LogoutView.as_view(template_name = 'relationship_app/logout.html'), name ='logout'),
]
