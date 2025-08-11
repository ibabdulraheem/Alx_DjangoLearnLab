from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Creating Post and User Models for the blog App
# class User(models.Model):
#   name = models.CharField(max_length=200)
  
class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  published_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
