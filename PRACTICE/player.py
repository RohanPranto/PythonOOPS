
players = []

# Read player data
for _ in range(4):
    playerId = int(input())
    playerName = input()
    runs = int(input())
    playerType = input()
    matchType = input()
    players.append({
        'playerId': playerId,
        'playerName': playerName,
        'runs': runs,
        'playerType': playerType,
        'matchType': matchType
    })

# Input for playerType and matchType to search
player_type = input()
match_type = input()

# findPlayerWithLowestRuns
lowest_runs = float('inf')
for player in players:
    if player['playerType'].lower() == player_type.lower():
        if player['runs'] < lowest_runs:
            lowest_runs = player['runs']

if lowest_runs == float('inf'):
    print("No such player")
else:
    print(lowest_runs)

# findPlayerByMatchType
filtered_players = []
for player in players:
    if player['matchType'].lower() == match_type.lower():
        filtered_players.append(player)

if not filtered_players:
    print("No Player with given matchType")
else:
    filtered_players.sort(key=lambda x: x['playerId'], reverse=True)
    for player in filtered_players:
        print(player['playerId'])
