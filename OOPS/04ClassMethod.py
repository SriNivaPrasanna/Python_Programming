'''
@classmethod
'''

class Emp:

    # class attribute
    company = "ABC"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def changeCompany(cls, new_company):
        cls.company = new_company

    def profile(self):
        print(f"Company is : {self.company}, name is: {self.name}, age is : {self.age}")


e1 = Emp("JOhn", 23)
e1.profile()
# Instance attribute
e1.company = "XYZ"
e1.profile()
Emp.changeCompany("SRC")
e2 = Emp("Jane" , 25)
e2.profile()

#Company is : ABC, name is: JOhn, age is : 23
#Company is : XYZ, name is: JOhn, age is : 23
#Company is : SRC, name is: Jane, age is : 25

