class Employee:
    company = "ABC"
    salary = 15000
    bonus = 500

    @property
    def totalSalary(self):
        return self.salary + self.bonus
    
    @totalSalary.setter
    def totalSalary(self, new_sal):
        self.bonus = new_sal - self.salary

    def get_sal(self):
        print("salary: ",self.salary)
    

e1 = Employee()
print(e1.totalSalary)
e1.totalSalary = 250000
print("Bonus: ", e1.bonus)
e1.get_sal()

#15500
#Bonus:  235000
#salary:  15000