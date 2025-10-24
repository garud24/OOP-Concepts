'''Create a Book class with attributes title, author, pages, and a method short_desc() that returns "Title by Author (N pages)".'''

class Book:
    
    # defnining __init__
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # function for short descriptions
    def short_desc(self):
        print(f"{self.title} by {self.author} ({self.pages} pages)")
        

#creating a object
p = Book("Mary: The Summoning", "Hillary Monahan", 250)

# calling short_desc() funciton
p.short_desc()

            