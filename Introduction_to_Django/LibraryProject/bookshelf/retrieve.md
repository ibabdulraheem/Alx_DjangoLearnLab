""" Retrieving and display all attributes of the book """
book = Book.objects.get(title = '1984')
for each_book in book:
  print(each_book)
