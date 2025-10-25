class Bag:
    items = []  # BAD: shared mutable default across all instances!

    def __init__(self):
        self.fixed = []  # GOOD: created per instance

a, b = Bag(), Bag()
a.items.append("Apples")
print(b.items)  # ['x']  <-- surprise!

# Fix by putting mutable defaults on the instance:
class SafeBag:
    def __init__(self, items=None):
        self.items = list(items) if items else []
a, b = SafeBag(), SafeBag()
a.items.append("Apples")
print(b.items) # This should be an empty list
print(a.items) # Here you should see ["Apples"]        