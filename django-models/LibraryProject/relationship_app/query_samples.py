
from relationship_app.models import Book
from relationship_app.models import Library
from relationship_app.models import Librarian, Author

""" Query all books by specific author """
author = Author.objects.get(author='author_name')
author.objects.filter(author='author')
# books = Book.objects.get(author = 'author_name').all()
# print(books)

""" List all books in a Library """
# ["Library.objects.get(name=library_name)"]
library=Library.objects.get(name="library_name")
library.books.all()




""" Retrieve the Librarian for a Library """
library = Library.objects.get(name ="librarian_name")



