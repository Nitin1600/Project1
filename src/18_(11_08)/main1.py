import books

keyword = "python"

data = books.search_books(keyword)

books.save_books(data, "books.txt")

print("Books saved successfully")