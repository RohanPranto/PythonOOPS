n=4
players=[]
for i in range(n):
    id=int(input())
    name=input()
    runs=int(input())
    type=input()
    match=input()
    players.append((id,name,runs,type,match))

search_type=input()
match_type=input()

#findPlayerWithLowestRuns 
min=None
for p in players:
    if p[3].lower() == search_type.lower():
        if min is None or p[2]<min[2]:
            min = p
if min is not None:
    print(min[2])
else:
    print("Not found") 

#find players id that matches match type
filter=[]
for t in players:
    if t[4]==match_type:
        filter.append(t[0])

if filter:
    filter.sort(reverse=True)
    for x in filter:
        print(x)
else:
    print("no player")