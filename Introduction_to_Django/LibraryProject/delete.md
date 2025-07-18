""" Delete the book you created and confirm the deletion by trying to retrieve all books again """
book = Book.objects.all()
book.delete()