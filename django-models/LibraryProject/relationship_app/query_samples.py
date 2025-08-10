
from relationship_app.models import Book
from relationship_app.models import Library
from relationship_app.models import Librarian, Author

""" Query all books by specific author """ 
# ["Author.objects.get(name=author_name)", "objects.filter(author=author)"]
author=Author.objects.get(author='author_name')
author.filter(author='author')

#"List all books in a Library
# ["Library.objects.get(name=library_name)"]
Library.objects.get(name="library_name").books.all()




""" Retrieve the Librarian for a Library """
librarian = Librarian.objects.get(library='library_name')



