from django.shortcuts import render
from .models import Book
from .models import Library
from relationship_app.models import Book
from relationship_app.models import Library
from django.views.generic import ListView
from django.urls import reverse_lazy

# Create your views here.
""" creating view for a book model """
def book_list (request):
  books = Book.objects.all()
  return render (request,books/'relationship_app/list_books.html')

class BookListView(ListView):
  model = Library
  books = Library.objects.get(name = 'library_name')
  for book in books:
    print(book)
  template_name = 'relationship_app/library_detail.html'
  success_url = reverse_lazy('book')
  
