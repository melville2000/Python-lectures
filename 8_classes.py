# Class is a blueprint for creating instances.
# Each unique employee that is created with the class is an instance of the class
# Self is a substitute for the instance variable

import datetime

class Employee:
    numOfEmop=0
    raise_amount=1.4
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=(first+'.'+last+'@company.com').lower()
        Employee.numOfEmop+=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
        
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)

    @classmethod
    #to edit the variable raise_amount
    def setraiseamount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    # Takes the empployee string and splits it and passes it in the class again
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        
    @staticmethod
    #Static method
    def isworkday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp_1 = Employee("Melville",'Dsouza',3000)
emp_2 = Employee('Nishil',"Visawadia", 9000)
emp_3 = Employee("Apurv","Patil",5000)

# Instance variables contain data that is unique to each instance

# print(emp_1.email)
# print(emp_2.first)
# print(emp_2.email)
# print(emp_2.fullname())
# Employee.fullname(emp_2)

#---------------Class Variables----------------------
# Class variables are variables that are shared among a all instances of a class
# Employee.raise_amount = 1.6 # Applies variable for the whole class
# emp_1.raise_amount = 1.5    # Applies variable for the instance only

# Employee.setraiseamount(1.9)
# print(Employee.raise_amount)
# Employee.raise_amount=1.8
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employee.numOfEmop)
#---------------Class methods----------------------
# Class methods take the class as the first argument
# 

# emp= "Ashok-Leyland-8000"
# emp_4=Employee.from_string(emp)
# print(emp_4.first)
# print(emp_4.last)
# print(emp_4.pay)
# print(emp_4.email)
#---------------STATIC methods----------------------
my_date=datetime.date(2022,11,14)
print(Employee.isworkday(my_date))





 
