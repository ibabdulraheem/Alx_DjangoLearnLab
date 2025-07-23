
from relationship_app.models import Book
from relationship_app.models import Library
from relationship_app.models import Librarian

""" Query all books by specific author """
books = Book.objects.get(author = 'author_name').all()
print(books)

""" List all books in a Library """
books_by_library = Library.objects.filter(name = 'library_name')
for books in books_by_library:
  print(books.name)



""" Retrieve the Librarian for a Library """
library = Library.objects.get(name ="librarian_name")



