from django.shortcuts import render
from .models import Book
from relationship_app.models import Book

# Create your views here.
""" creating view for a book model """
def book_list (request):
  books = Book.objects.all()
  list_of_books = (f"{books.title} and {books.author}")
  return render (request,list_of_books)
