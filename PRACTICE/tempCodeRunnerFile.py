n=int(input())
iceCream=[]
for i in range(n):
    id=int(input())
    price=int(input())
    name=input()
    quantityInGms=int(input())
    category=input()
    iceCream.append([id,price, name, quantityInGms, category])

sorted_iceCream = sorted(iceCream, key=lambda x: x[1])

# Print the lowest priced ice cream details
print(sorted_iceCream[0][0])
print(sorted_iceCream[0][1])
print(sorted_iceCream[0][2])
print(sorted_iceCream[0][3])
print(sorted_iceCream[0][4])
