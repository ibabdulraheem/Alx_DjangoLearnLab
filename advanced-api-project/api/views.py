from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework



# Create your views here.  
""" Creating Custom Generic views for the model Book"""

class CustomBookListView(generics.ListApiView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_class =BookFilter

class CustomBookDetailView(generics.DetailApiView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class CustomBookCreateView(generics.CreateApiView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

class CustomBookUpdateView(generics.UpdateApiView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]

class CustomBookDeleteView(generics.DeleteApiView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
