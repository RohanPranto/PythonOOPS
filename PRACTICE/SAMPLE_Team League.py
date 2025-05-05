class Team:
    def __init__(self, owner: str, value: float, id: int, name: str):
        self.owner = owner
        self.value = value
        self.id = id
        self.name = name

class League:
    def __init__(self, leagueName: str, teamList: list):
        self.leagueName = leagueName
        self.teamList = teamList

    def findMinimumTeamById(self):
        if not self.teamList:
            return None
        min_team = self.teamList[0]
        min_id = self.teamList[0].id
        for team in self.teamList:
            if team.id < min_id:
                min_id = team.id
                min_team = team
        return min_team

if __name__ == "__main__":
    n = int(input())
    teams = []
    for _ in range(n):
        owner = input()
        value = float(input())
        team_id = int(input())
        name = input()
        team = Team(owner, value, team_id, name)
        teams.append(team)

    league_name = "Super League"  # You can use any random string
    league = League(league_name, teams)

    minimum_id_team = league.findMinimumTeamById()

    if minimum_id_team:
        print(minimum_id_team.owner)
        print(minimum_id_team.value)
        print(minimum_id_team.id)
        print(minimum_id_team.name)
    else:
        print("No Data Found")