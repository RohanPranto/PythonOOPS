# RCB
n = int(input())

# Initialize an empty list to store team data
team = []

# Reading team details
for i in range(n):
    owner = input()
    value = float(input())
    id = int(input())
    name = input()
    # Store the team details as a tuple in the team list
    team.append((owner, value, id, name))

# Initialize variables to track the team with minimum id
min_team = None

# Find the team with the minimum id
if team:
    min_team = team[0]  # Assume the first team is the minimum initially
    for t in team[1:]:
        if t[2] < min_team[2]:  # Compare ids
            min_team = t

# Output results
if min_team is None:
    print("No Data Found")
else:
    print(min_team[0])  # Owner
    print(min_team[1])  # Value
    print(min_team[2])  # Id
    print(min_team[3])  # Name
