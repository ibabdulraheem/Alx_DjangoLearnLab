from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

""" creating 2 data models: Book and Author"""
class Author(models.Model):
  name = models.CharField(max_length=100)

class Book(models.Model):
  title = models.CharField(max_length=200)
  publication_year = models.IntegerField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

