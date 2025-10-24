'''exercise 2

Write a Team class that safely tracks a per-instance list members and a class attribute min_size=5.'''

class Team:
    min_size = 5
    
    def __init__(self):
        self.members = []  # instance variable unique to each team

t1 = Team()
t2 = Team()

t1.members.append("Bob")
t2.members.append("Cat")
print(t1.members)
print(t2.members)
print(Team.min_size) 

t1.members.append("Builder")
t1.members.append("Bullet")
print(t1.members)
     