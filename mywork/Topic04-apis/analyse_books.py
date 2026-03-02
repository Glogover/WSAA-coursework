from book_API_DAO import getAllBooks

books = getAllBooks()
total = 0
count = 0
for book in books:
    if book["price"] is not None: # check if price is not None to avoid errors when adding
        total += book["price"]
        count += 1

print ("Average price of", count, "books is ", total/count)


