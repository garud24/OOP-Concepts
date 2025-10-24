'''1) classes, objects, attributes, and __init__'''

class Player:
    # class attribute (shared by all instances)
    species = "Human"
    
    def __init__(self, name, level = 1):
        # instance attributes (each object has its own copy)
        self.name = name
        self.level = level
    
    def level_up(self):
        self.level += 1

p = Player("Himanshu")
print(p.name, p.level, Player.species)   

# calling level_up()
p.level_up()
print(p.name, p.level, Player.species)   
    
        