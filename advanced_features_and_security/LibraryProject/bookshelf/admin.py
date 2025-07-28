from django.contrib import admin
from .models import CustomUser,CustomUserManager,CustomUserAdmin

# Register your models here.

admin.site.register(CustomUser ,CustomUserAdmin )




