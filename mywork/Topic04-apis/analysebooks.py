from bookapidao import getAllBooks

books = getAllBooks()
total = 0
count = 0
for book in books:
    if book["price"] is not None:
     total += book["price"]
    count += 1

# or if you want to be fancier
# total = sum(book["price"] for book in books)
# count = len(books)

print ("Average price of", count, "books is ", total/count )

