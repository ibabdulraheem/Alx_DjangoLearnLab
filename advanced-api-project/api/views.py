from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer

# Create your views here.  
""" Creating Custom Generic views for the model Book"""

class CustomBookListView(generics.ListApiView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class CustomBookDetailView(generics.DetailApiView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class CustomBookCreateView(generics.CreateApiView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class CustomBookUpdateView(generics.UpdateApiView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class CustomBookDeleteView(generics.DeleteApiView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
