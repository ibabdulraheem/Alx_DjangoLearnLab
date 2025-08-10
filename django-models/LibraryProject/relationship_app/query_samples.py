
from relationship_app.models import Book
from relationship_app.models import Library
from relationship_app.models import Librarian, Author

""" Query all books by specific author """ 
# books = Book.objects.get(author = 'author_name').all()
# print(books)
author=Author.objects.get(author='author_name')
author.filter(author='author')

#"List all books in a Library
# ["Library.objects.get(name=library_name)"]
Library.objects.get(name="library_name").books.all()




""" Retrieve the Librarian for a Library """
library = Library.objects.get(name ="librarian_name")



