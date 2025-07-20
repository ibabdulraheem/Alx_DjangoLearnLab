from django.shortcuts import render
from .models import Book
from relationship_app.models import Book

# Create your views here.
""" creating view for a book model """
def book_list (request):
  books = Book.objects.all()
  template_name = 'list_books.html'
  return render (books/template_name)
