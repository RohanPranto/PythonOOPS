n= int(input())
books_details=[]
for i in range(n):
    pages=int(input())
    price = int(input())
    author = input()
    id = int(input())
    title= input()
    books_details.append((pages,price,author,id,title))

min = None
if n>0:
    min = books_details[0]
    for books in books_details:
        if books[3]<min[3]:
            min = books  #minimum id book

print(f"{min[0]}\n{min[1]}\n{min[2]}\n{min[3]}\n{min[4]}")

if n>0:
    id_list=[]
    for t in books_details:
        id_list.append(t[3])
        id_list.sort()

    for s in id_list:
        print(s)
else:
    print("No book")

