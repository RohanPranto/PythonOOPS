n = 4
details = []
for i in range(n):
    playerId = int(input())
    playerName = input()
    runs = int(input())
    playerType = input()
    matchType = input()
    details.append((playerId, playerName, runs, playerType, matchType))

search_type = input()
search_match = input()

#minimum run find
min_run = None
for run in details:
    if run[3].lower() == search_type.lower():
        if min_run is None or run[2] < min_run: #min_run is None: This is true for the first player since min_run is initially None. It ensures that we set min_run to the first player's runs during the first iteration. THEN, run[2] < min_run: For subsequent players, this checks if the current player's runs (run[2]) are less than the previous minimum (min_run). If they are, we update min_run to the new lower value.
            min_run = run[2]

if min_run is not None:
    print(min_run)
else:
    print("No such player")


#find player id as search_match and print in desc order
filter=[]
for ids in details:
    if ids[4].lower()==search_match.lower():
        filter.append(ids[0])


    

#sort in desc
if filter:
    filter.sort(reverse=True)
    for x in filter:
        print(x)
else:
    print("Not a single player")