n=int(input())
iceCream=[]
for i in range(n):
    id=int(input())
    price=int(input())
    name=input()
    quantityInGms=int(input())
    category=input()
    iceCream.append([id,price, name, quantityInGms, category])

#first output
sorted_iceCream = sorted(iceCream, key=lambda x: x[1])
if sorted_iceCream:
    print(f"{sorted_iceCream[0][0]}\n{sorted_iceCream[0][1]}\n{sorted_iceCream[0][2]}\n{sorted_iceCream[0][3]}\n{sorted_iceCream[0][4]}")
else:
    print("No Data Found.")

#second output
sorted_ids=sorted(iceCream, key=lambda x: x[0])
if sorted_ids:
    print(f"{sorted_ids[0][0]}\n{sorted_ids[1][0]}\n{sorted_ids[2][0]}\n{sorted_ids[3][0]}\n{sorted_ids[4][0]}")
else:
    print("No Data Found.")