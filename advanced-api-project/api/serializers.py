from rest_framework import serializers
from .models import Author, Book



""" Creating Serializers for the Author and Book """
#  ["class Author(models.Model)", "class Book(models.Model)"]

class AuthorSerializer (serializers.ModelSerializer):
  class meta:
    model = Author
    field = ['name']

class BookSerializer (serializers.ModelSerializer):
  class meta:
    model = Book
    field = '__all__'