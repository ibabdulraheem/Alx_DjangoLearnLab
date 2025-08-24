from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user is created 
class CustomUser(AbstractUser):
  bio = models.TextField(blank=True, null=True)
  profile_picture = models.ImageField(upload_to='profiles/',blank=True, null=True)
  followers = models.ManyToManyField('self',symmetrical=False,related_name='following',blank=True)
  following = models.ManyToManyField('self',symmetrical=False,related_name='followers',blank=True) #Added field

  def __str__(self):
    return self.username



