
from relationship_app.models import Book
from relationship_app.models import Library
from relationship_app.models import Librarian

""" Query all books by specific author """
books = Book.objects.get(author = 'author_name')
print(books)

""" List all books in the Library """
library = Library.objects.all()
for books in library:
  print(books)

""" Retrieve the Librarian for a Library """
librarian = Librarian.objects.get(name = "librarian_name")



