n = int(input())  # Number of teams
team = []

# Reading the team information
for i in range(n):
    owner = input()
    value = float(input())
    id = int(input())
    name = input()
    
    # Storing each team's data as a tuple (owner, value, id, name)
    team.append((owner, value, id, name))

# Initialize the max team by ID
if team:
    max_team = team[0]
    for i in team:
        if max_team[2] < i[2]:  # Comparing team IDs
            max_team = i
    # Output the team with the maximum ID
    print(max_team[0])  # Owner
    print(max_team[1])  # Value
    print(max_team[2])  # ID
    print(max_team[3])  # Name
else:
    print("No Data Found")

# Sorting the team by ID
if team:
    sorted_team = sorted(team, key=lambda x: x[2])  # Sorting by ID
    for i in sorted_team:
        print(i[2])  # Print team ID
else:
    print("No data")
