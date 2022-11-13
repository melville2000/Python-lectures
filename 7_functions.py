def hello():
    pass        # is used to leav a function blank to fill in later

def hello1():
    return "hello fucnction"


#print("hello fucnction")
#print("hello fucnction")
#print("hello fucnction")
#print("hello fucnction")

hello1()
hello1()
hello1()
hello1()
# DRY i.e. Dont Repeat Yourself

print(hello1())
#---------------------------------------------------------
def hello_func(greeting,name="Melville"):
    return "{}, {}".format(greeting, name)

print(hello_func("Username"))
#---------------------------------------------------------
def student(*args,**kwargs):
    print(args)
    print(kwargs)

#student("math", "phy",name="Andy",Age=33)

courses=("Math","art", 'Physics', "History")
info={'name':'Andy','age':22}

student(*courses,**info)
#('Math', 'art', 'Physics', 'History')
#{'name': 'Andy', 'age': 22}
#---------------------------------------------------------
# Single * is used to unpack Lists
# Double ** is used to unpack Dcts