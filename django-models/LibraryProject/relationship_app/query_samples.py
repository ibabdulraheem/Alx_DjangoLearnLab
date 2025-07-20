""" Query all books by specific author """
from relationship_app.models import Book
from relationship_app.models import Library
from relationship_app.models import Librarian


book = Book.objects.all(author = 'author')
book.save()

""" List all books in the Library """
library = Library.objects.all()
for books in library:
  print(books)

""" Retrieve the Librarian for a Library """
librarian = Librarian.objects.get(name = "library_name")



