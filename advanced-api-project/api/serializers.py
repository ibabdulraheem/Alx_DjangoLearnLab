from rest_framework import serializers
from .models import Author, Book
import datetime



""" Creating Serializers for the Author and Book """

class AuthorSerializer(serializers.ModelSerializer):
  class meta:
    model = Author
    field = ['name']

class BookSerializer(serializers.ModelSerializer):
  class meta:
    model = Book
    field = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
# Creating a Nested Serializer 
class BookSerializer(serializers.ModelSerializer):
   name = AuthorSerializer(many = True, read_only = True)
   class meta:
      model = Book
      field = '__all__'