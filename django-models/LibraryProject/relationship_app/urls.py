from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
  path ('hello/',views.book_list, name ='hello'),
  path ('about/',views.BookListView.as_view(), name = 'about'),
]
