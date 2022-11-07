""" def hello():
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
 """
""" def hello_func(greeting,name="Melville"):
    return "{}, {}".format(greeting, name)

print(hello_func("Username"))
 """
""" def addition(n1,n2):
    return n1+n2

addition(1,2) """

def student(*args,**kwargs):
    print(args)
    print(kwargs)

#student("math", "phy",name="Andy",Age=33)


courses=("Math","art", 'Physics', "History")
info={'name':'Andy','age':22}

student(*courses,**info)