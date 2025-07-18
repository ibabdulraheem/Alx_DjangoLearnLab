""" Delete the book you created and confirm the deletion by trying to retrieve all books again """
from bookshelf.models import Book
book = Book.objects.all()
book.delete()