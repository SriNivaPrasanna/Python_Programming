'''
OOPS -> Object Oriented Programming System

class -> blueprint
object -> real world entity

property -> variables
methods -> functions

4 Pillars of OOPS
encapsulation -> It binds properties and methods under sigle entity
abstraction -> hiding unnecessary data 
inheritance -> child class (derived class) inherits from the super class (base class)
Polymorphism (poly (many) + morph (forms))

'''

class Employee:
    
    def greet(self):
        print("WELCOME")

e1 = Employee()
e2 = Employee()
print(e1)
print(type(e1))
#<__main__.Employee1 object at 0x00000189C5F02B10>
#<class '__main__.Employee1'>
e1.greet()
# whenever we call a method in a class, we pass object reference at the time of calling
e2.greet()
#WELCOME
#WELCOME