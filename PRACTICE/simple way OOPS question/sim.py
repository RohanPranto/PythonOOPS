n = int(input()) #number of input
sim = []

for i in range(n):
    simId = int(input())
    customerName = input()
    balance = float(input())
    ratePerSecond = float(input())
    circle = input()
    sim.append([simId,customerName,balance,ratePerSecond,circle])

circle1=input() #old circle
circle2=input() #new circle

transferred = []

for i in sim:
    if i[4].lower()==circle1.lower():
        transferred.append([i[0],i[1],circle2,i[3]])
    
    transferred.sort(key=lambda x:x[3], reverse=True)
    
if transferred:
    for t in transferred:
        print(f"{t[0]} {t[1]} {circle} {t[3]}")
else:
    print("No data found")