from django.shortcuts import render
from .models import Book
from relationship_app.models import Book

# Create your views here.
""" creating view for a book model """
def book_list (request):
  books = Book.objects.all()
  return render (request,'relationship_app/list_books.html')
