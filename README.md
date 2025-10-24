# Object Oriented Programming in Python
## 1) classes, objects, attributes, and __init__
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
## 2) instance vs class variables; mutability gotchas

```
class Bag:
    items = []  # BAD: shared mutable default across all instances!

    def __init__(self):
        self.fixed = []  # GOOD: created per instance

a, b = Bag(), Bag()
a.items.append("x")
print(b.items)  # ['x']  <-- surprise!

```
- Fix by putting mutable defaults on the instance:
```
class SafeBag:
    def __init__(self, items=None):
        self.items = list(items) if items else []

```

- The problem (the “gotcha”): 

    If you define a mutable class variable (like a list or dict), it’s shared across all objects, not copied for each instance.

    This can lead to unexpected behavior because changing it in one object changes it for all.