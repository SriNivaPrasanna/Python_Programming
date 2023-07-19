'''
methods without self keyword
these methods are independent of the object calling it
'''

class Employee:

    def __init__(self, n , age = "NA"):
        self.n = n
        self.age = age
    
    @staticmethod
    def greet():
        print("WELCOME")
    
    def getName(self):
        return self.n , self.age

obj = Employee("John", 23)
print(obj.getName())

obj2 = Employee("Jane")
print(obj2.getName())

obj.greet()
obj2.greet()

#('John', 23)
#('Jane', 'NA')
#WELCOME
#WELCOME