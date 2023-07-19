'''
Inheritance -> Child (derived) class inherits the methods and attributes from base (super) class

single inheritance
multiple inheritance
multilevel inheritance

'''

# TODO: Single Inheritance

class A:
    def greet(self):
        print("I am greet in class A")
class B (A):
    def greet2(self):
        print("I am greet in class B")

obj = B()
obj.greet()   #I am greet in class A
obj.greet2()  #I am greet in class B

obj = A()
obj.greet()  #I am greet in class A
obj.greet2()   # Attribute Error

# TODO: Multile inheritance
class A:
    def greet(self):
        print("I am greet in class A")


class B:
    def greet2(self):
        print("I am greet in class B")

class C (B, A):
    def greet3(self):
        print("I am greet in class C")

obj = C()
obj.greet()
obj.greet2()
obj.greet3()

#I am greet in class A
#I am greet in class B
#I am greet in class C


# TODO: Multilevel Inheritance
class A:
    def greet(self):
        print("I am greet in class A")


class B(A):
    def greet2(self):
        print("I am greet in class B")

class C (B):
    def greet3(self):
        print("I am greet in class C")

obj = C()
obj.greet()
obj.greet2()
obj.greet3()
obj2 = B()
obj2.greet()
obj.greet2()


#I am greet in class A
#I am greet in class B
#I am greet in class C
#I am greet in class A
#I am greet in class B