class Team:
    def __init__(self, owner: str, value: float, id: int, name: str):
        self.id = id
        self.name = name
        self.owner = owner
        self.value = value

class League:
    def __init__(self, leagueName: str, teamList: list):
        self.leagueName = leagueName
        self.teamList = teamList

    def findMaximumTeamById(self):
        if not self.teamList:
            return None
        max_team = self.teamList[0]
        max_id = self.teamList[0].id
        for team in self.teamList:
            if team.id > max_id:
                max_id = team.id
                max_team = team
        return max_team

    def sortTeamById(self):
        if not self.teamList:
            return None
        return sorted(self.teamList, key=lambda team: team.id)

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

    league_name = "MyLeague"
    league = League(league_name, teams)

    max_id_team = league.findMaximumTeamById()
    if max_id_team:
        print(max_id_team.owner)
        print(max_id_team.value)
        print(max_id_team.id)
        print(max_id_team.name)
    else:
        print("No Data Found")

    sorted_teams = league.sortTeamById()
    if sorted_teams:
        for team in sorted_teams:
            print(team.id)
    else:
        print("No Data Found")