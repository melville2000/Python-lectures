class School():
    def __init__(self,first,last,phone):
        self.first =  first
        self.last = last
        self.phone = phone
        self.email = (first +"."+ last + "@school.com").lower()
    
    def fullName(self):
        return '{} {}'.format(self.first,self.last)
    
    def printInfo(self):
        return self.fullName() ,self.email, self.phone

class Student(School):
    def __init__(self, first, last, phone, rollNo, std, div, subjects=None):
        super().__init__(first, last, phone)
        self.rollNo = rollNo
        self.std = std
        self.div = div
        if subjects is None:
            self.subjects = []
        else:
            self.subjects = subjects

class Teacher(School):
    totalTeach=0
    def __init__(self, first, last, phone, cla, subjects=None):
        super().__init__(first, last, phone)
        self.cla = cla
        if subjects is None:
            self.subjects = []
        else:
            self.subjects=subjects
        Teacher.totalTeach += 1

class Subjects():
    def addSub(self, sub):
        if sub not in self.subjects:
            self.subjects.append(sub)
            
    def removeSub(self, sub):
        if sub in self.subjects:
            self.subjects.remove(sub)
    
    def printSub(self):
        for sub in self.subjects:
            print("-->", sub)


stud1= Student('Apurv','Patil', 8797022345, 1,7,'A')
teach1= Teacher('Mustafa','Khan',9876543210,9,['math','science','english'])
teach2 = Teacher('Nishil','Visawadia',9877665544, 5,['history','geography','english'])
# print(teach1.printInfo())
# print(teach2.printInfo())
# print(teach1.printSub())
# print(Subjects.printSub(teach1))
# print(Teacher.totalTeach)

teach2.addSub('morals')
print(teach2.printSub())