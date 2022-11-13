class Employee:
    raise_amount = 1.04
    number_employees = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first +"."+ last+"@company.com").lower()
        Employee.number_employees+=1
    
    def fullName(self):
        return '{} {}'.format(self.first,self.last)
    
    def applyRaise(self):
        self.pay=int(self.pay * self.raise_amount)
    
    def __repr__(self) -> str:
        # Used when we need print the instance var for devs
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self) -> str:
        # Used to show the user the valuse of the var
        return "{} - {}".format(self.fullName(),self.email)


class Developer(Employee):
    raise_amount=1.10
    def __init__(self,first,last,pay,progLang):
        super().__init__(first,last,pay)  #  Passes the args into the parent clas to handle
        self.progLang = progLang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees =  []
        else:
            self.employees = employees

    def addEmp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def removeEmp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmployee(self):
        for emp in self.employees:
            print("-->", emp.fullName())

#----------------------------------------------------------
dev_1=Developer('Melivlle','Dsouza',20000,"Python")
dev_2=Developer('Mustafa','Khan',10000,"Java")
mgr_1=Manager('Nishil','Visawadia',40000,[dev_1])
mgr_2=Manager('Apurv','Patil',30000,[dev_1,dev_2])

# mgr_1.removeEmp(dev_2)
# mgr_1.printEmployee()

# print(issubclass(Manager, Employee))
# print(dev_1.email)
# print(dev_1.progLang)


# print(dev_1.pay)
# dev_1.applyRaise()
# print(dev_1.pay)

print(repr(dev_1))