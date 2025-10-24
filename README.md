# Object Oriented Programming in Python
# 1) classes, objects, attributes, and __init__
- A class is a blue print and an object(instance) is a build thing

```
class Player:
    # class attribute (shared by all instances)
    species = "Homo sapiens"

    def __init__(self, name, level=1):
        # instance attributes (each object has its own copy)
        self.name = name
        self.level = level

    def level_up(self):
        self.level += 1

p = Player("Himanshu")
p.level_up()
print(p.name, p.level, Player.species)  # Himanshu 2 Homo sapiens
```