# Read number of books
n = int(input())

# Create the book list
bookList = []
for _ in range(n):
    book = {}
    book['pages'] = int(input())
    book['price'] = int(input())
    book['author'] = input().strip()
    book['id'] = int(input())
    book['title'] = input().strip()
    bookList.append(book)

# Find book with minimum id
minBook = None
if len(bookList) > 0:
    minBook = bookList[0]
    for book in bookList[1:]:
        if book['id'] < minBook['id']:
            minBook = book

if minBook is not None:
    print(minBook['pages'])
    print(minBook['price'])
    print(minBook['author'])
    print(minBook['id'])
    print(minBook['title'])
else:
    print("No Data Found")

# Sort books by id
if len(bookList) > 0:
    sorted_ids = []
    for book in bookList:
        sorted_ids.append(book['id'])
    sorted_ids.sort()
    for i in sorted_ids:
        print(i)
else:
    print("No Data Found")
