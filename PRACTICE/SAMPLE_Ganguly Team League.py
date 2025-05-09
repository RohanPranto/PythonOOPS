class Team:
    def __init__(self,owner,value,id,name):
        self.id= id
        self.name = name
        self.owner = owner
        self.value=value

class League:
    def __init__(self,leagueName,teamList):
        self.leagueName= leagueName
        self.teamList = teamList

    def findMaximumTeamById(self):
        if self.teamList is None:
            return None
        else:
            max=self.teamList[0]
            for i in self.teamList:
                if max.id< i.id:
                    max=i
            return max



    def sortTeamById(self):
        if self.teamList is None:
            return None
        else:
            return sorted(self.teamList, key=lambda x:x.id)



n=int(input())
team=[]
for i in range(n):
    owner=input()
    value=float(input())
    id=int(input())
    name=input()
    t=Team(owner,value,id,name)
    team.append(t)

    s="My League"
    l=League(s, team)

    ans2= l.findMaximumTeamById()
    if ans2 is None:
        print("No Data Found")
    else:
        print(ans2.owner)
        print(ans2.value)
        print(ans2.id)
        print(ans2.name)

    ans1=l.sortTeamById()
    if ans1 is None:
        print("No data")
    else:
        for i in ans1:
            print(i.id)