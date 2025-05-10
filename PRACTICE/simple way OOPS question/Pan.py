n=int(input())
pan=[]
for i in range(n):
    id=input()
    material=input()
    brand=input()
    price=int(input())
    capacity=int(input())
    pan.append((id,material,brand,price,capacity))

search_material = input()
search_brand = input()

#costliest pan
for i in pan:
    max= None
    max_price=-1
    for i in pan:
        if i[1] == search_material and i[3] > max_price:
            max=i


if max is not None:
    print(max[0])
else:
    print("No pan found")




#discounted price
discounted=None
for pans in pan:
    if pans[2]==search_brand:
        if pans[4]>500:
            discounted=int(pans[3]*0.80)
        elif pans[4]>1000:
            discounted=int(pans[3]*0.74)
        else:
            discounted=pans[3]
        break

if discounted is not None:
    print(discounted)
else:
    print("Not found bro")