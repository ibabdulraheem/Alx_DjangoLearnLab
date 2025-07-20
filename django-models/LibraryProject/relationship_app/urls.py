from django.urls import path
from . import views
from .views import book_list, BookListView

urlpatterns = [
  path ('hello/',views.book_list, name ='hello'),
  path ('about/',views.BookListView.as_view(), name = 'about'),
]
