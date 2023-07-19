'''
Multilevel Inheritance -> there is a heirarchy in which classes are inherited
'''

class Human:
    eyes = 2

    def breathe(self):
        print("I am breathing human!")
    
class Employee(Human):
    company = "ABC"

    def breathe(self):
        print("Breathing Employee")
        super().breathe()


class Programmer(Employee):
    language = "Python"

    def breathe(self):
        super().breathe()
        print("Hardly gets the time to breathe!")

p1 = Programmer()
p1.breathe()

#Breathing Employee
#I am breathing human!
#Hardly gets the time to breathe!