n= int(input())
room_details=[]
for i in range(n):
    roomId= int(input())
    numberOfRooms = int(input())
    cabFacility=input()
    bill=int(input())
    name=input()
    room_details.append((roomId,numberOfRooms,cabFacility,bill,name))

threshold=int(input())
total_bill=0
cab_motel=[]
#cab facility yes motels
for j in room_details:
    if j[2].lower()=="yes":
        print(j[4])
        cab_motel.append(j[4])

if len(cab_motel)==0:
    print("no motel found with cab facility")
billa=[]
for k in room_details:
    if k[1]>threshold:
        total_bill+=k[3]
        billa.append(k[4])

if len(billa):
    print(total_bill)
else:
    print("Threshold didnt cross")


