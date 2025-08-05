from django.db import models

# Create your models here.

""" Creating my model by way of creating class """
class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publication_year = models.IntegerField()
