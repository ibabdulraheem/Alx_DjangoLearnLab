from django.contrib import admin
from .models import Book     # import Book model


# Register your models here.
admin.site.register(Book)     #  Register the Book Model with the Django Admin

@admin.register(Book)          # Another way to register Model to enable customizations
class BookAdmin(admin.ModelAdmin):
  list_display = ('title','author','publication_year') # columns in the list view of your Book model in the admin interface.
  list_filter = ('publication_year','author') # This attribute enables filters on the right sidebar of the admin list view.
  search_fields = ('title','author') # 	This attribute adds a search box at the top of the admin list view.
