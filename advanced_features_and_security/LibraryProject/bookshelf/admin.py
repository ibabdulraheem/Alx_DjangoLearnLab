from django.contrib import admin
from .models import CustomUser,CustomUserAdmin
from bookshelf.models import Books

# Register your models here.

# admin.site.register (CustomUser,CustomUserAdmin)
["admin.site.register(CustomUser, CustomUserAdmin)"]

admin.site.register(Books)




