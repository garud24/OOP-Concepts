'''This is to demonstrate the difference between the Instatnce method Vs Class method'''
from datetime import date

class Person:
    
    # defining the __init__()
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Adding a description function
    def description(self):
        return f"The name of the person is: {self.name} and the age is: {self.age}."
    
    '''What if the user don't want to pass his age what if he want to pass his age by the birth_year'''
    @classmethod
    def age_from_year(cls, name, birth_year):
        current_year = date.today().year
        age = current_year - birth_year
        
        return cls(name, age)
    
    

# Writing the main function
if __name__ == "__main__":
    
    # This was an Instance method
    p = Person('Rajesh', 22)
    
    print(p.description()) 
    
    # This was an classMethod
    himanshu = Person.age_from_year("Himanshu", 1999)
    print(himanshu.description())
    
    
          