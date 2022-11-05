
language =  ""

if language == "python":
    print("Python is present")
elif language=="java":
    print("Java is present")
else:
    print("Not Present")

#---------BOOLEAN OPERATORS---------
    # and   Both statments should be true
    # or    Either one of the statments should be true
    # not   Turns True into False or False into True

user = "Admin"
status = False

if not status:
    print("Logged in sucessfully")

else :
    print("Login failed")   #Login failed

#---------is OPERATOR---------
    # the 'is' operator is used to show the location of a variable that is stored in the memory.
a = [1,3,2]
b = [1,3,2]

print(id(a))    # 140416362324800
print(id(b))    # 140416362401856
print(a)        # [1, 3, 2]
print(b)        # [1, 3, 2]

#---------FALSE VALUES---------
    # False.
    # None.
    # Zero of any numeric type.
    # Any empty sequence, '',(),[].
    # Any empty mapping, {}.

condition = 'test'

if condition:
    print("Evaluated to true")

else:
    print("Evaluated to false")