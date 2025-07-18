""" Retrieving and display all attributes of the book """
book = Book.objects.all()
for each_book in book:
  print(each_book)
