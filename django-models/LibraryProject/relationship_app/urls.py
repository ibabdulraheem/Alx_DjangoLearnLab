from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
  path ('book_list/',views.book_list, name ='book_list'),
  path ('books_by_library/',views.BookListView.as_view(), name = 'book_by_library'),
]
