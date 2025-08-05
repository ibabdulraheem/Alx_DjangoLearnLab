
from bookshelf.models import Book
from bookshelf.models import Library
from bookshelf.models import Librarian

""" Query all books by specific author """
books = Book.objects.get(author = 'author_name').all()
print(books)

# """ List all books in a Library """
library = Library.objects.get(name="library_name")
library.books.all()




""" Retrieve the Librarian for a Library """
library = Library.objects.get(name ="librarian_name")



