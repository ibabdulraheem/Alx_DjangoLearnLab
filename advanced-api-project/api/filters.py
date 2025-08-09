import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
  class meta:
    model = Book
    field = {
      'title':['exact', 'icontains'],
      'author': ['exact','icontains'],
      'publication_year': ['exact','gte','lte']
    }