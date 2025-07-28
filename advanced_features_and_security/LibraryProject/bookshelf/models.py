from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.backends import BaseBackend


class UserSignUp(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(null = True)
    profile_photo = models.ImageField(null=True,blank=True)