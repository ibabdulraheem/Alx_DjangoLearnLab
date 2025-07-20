from django.urls import path
from . import views

urlpatterns = [
  path ('hello/',views.book_list, name ='hello'),
  path ('about/',views.BookListView.as_view(), name = 'about'),
]
