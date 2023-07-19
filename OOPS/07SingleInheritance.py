'''
Single Inheritance
One child class will be inheriting from a parent class
'''

class Employee:
    company = "ABC"

    def onboarding(self):
        print("Welcome on board!!")
    

class Programmer(Employee):
    language = "Python"

    def debug(self):
        print("We are debugging!!")

class Finance(Employee):
    def profile(self):
        print("We handle accounts!!")

p1 = Programmer()
p1.debug()  #We are debugging!!

p1.onboarding()  #Welcome on board!!