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

- Here is another example to demonstarte between Class method Vs Instance Method Vs Static method
    - Instance method vs Static method
    ```
    '''This example is to demonstate the difference betweeen Static Method vs Instance Method'''

    class Calculator:

        # Added a constructor
        def __init__(self, version):
            self.version = version

        # Adding a description method
        def description(self):
            return f"Currently running on the following version, {self.version}"

        # Adding static method
        @staticmethod
        def add_numbers(*numbers):
            return sum(numbers)

    # So, you can see the static method is like normal function, it can be written inside or outside the class
    # def add_numbers(*numbers):
    #     return sum(numbers)


    # Main function
    if __name__ == '__main__':

        instance1 = Calculator(10)
        instance2 = Calculator(20)
        '''
        This is the instatnce method, which depends on the instances, each instances will have its own instance
        '''
        print(instance1.description())
        print(instance2.description())   

        '''
        Calling static method, the static method does not need to have instance as you can see from the function call,
        it can work inside of the class or outside of the class
        '''
        print(Calculator.add_numbers(10,230,10)) # when associated with class Calculator

        # print(add_numbers(10,230,10)) when not associated with the class 
    ```

    - Instance method vs Class method
    The class method is nto taking the self, it is taking the first argument as the cls, which tell us that the class is directlty affected

    ```
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
   
    ```