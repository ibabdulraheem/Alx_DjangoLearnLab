from django.contrib import admin
from .models import Book     # import Book model


# Register your models here.
admin.site.register(Book)     #  Register the Book Model with the Django Admin

@admin.register(Book)          # Another way to register Model to enable customizations
class BookAdmin(admin.ModelAdmin):
  list_display = ('title','author','publication_year')  
  list_filter = ('publication_year','author')
  search_fields = ('title','author')
