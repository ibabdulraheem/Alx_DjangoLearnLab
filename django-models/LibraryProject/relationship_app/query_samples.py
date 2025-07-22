
from relationship_app.models import Book
from relationship_app.models import Library
from relationship_app.models import Librarian

""" Query all books by specific author """
books = Book.objects.get(author = 'author_name').all()
print(books)

""" List all books in a Library """
books=Library.objects.get(name="library_name")
print(books)


""" Retrieve the Librarian for a Library """
library = Library.objects.get(name ="librarian_name")



