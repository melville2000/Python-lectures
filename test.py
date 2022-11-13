class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)

    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print('Delete name')
        self.first = None
        self.last = None 

emp1=Employee("John","Dsouza")

emp1.fullName = 'Joshua Mathew'

print(emp1.fullName)
del(emp1.fullName)
print(emp1.fullName)
# print(emp1.first)
# print(emp1.last)