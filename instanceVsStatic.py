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
   