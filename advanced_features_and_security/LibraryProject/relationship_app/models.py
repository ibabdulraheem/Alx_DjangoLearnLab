from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    date_of_birth = models.IntergerField(unique = True)
    profile_photo = models.ImageField(default = 'default.jpg')