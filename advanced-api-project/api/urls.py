from django.urls import path
from .views import (
    CustomBookListView,
    CustomBookCreateView,
    CustomBookDetailView,
    CustomBookUpdateView,
    CustomBookDeleteView
)

urlpatterns = [
  #  # URL for listing all books and creating a new book
    path('books/', CustomBookListView.as_view(), name='book-list'),
    path('books/create/', CustomBookCreateView.as_view(), name='book-create'),

    # URL for retrieving, updating, and deleting a specific book
    path('books/<int:pk>/', CustomBookDetailView.as_view(), name='book-detail'),
    path('books/update/', CustomBookUpdateView.as_view(), name='book-update'),
    path('books/delete/', CustomBookDeleteView.as_view(), name='book-delete'),
]