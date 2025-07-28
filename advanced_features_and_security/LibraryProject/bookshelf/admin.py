from django.contrib import admin
from .models import CustomUser,BaseUserAdmin

# Register your models here.

admin.site.register(CustomUser, BaseUserAdmin)


