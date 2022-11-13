#-------LISTS DEFINATION-------
# Lists are used to store multiple data in under 1 variable
# [ ] are used to make a list
# Lists are ordered, changable and allow duplicates
# List items are indexed, the first item has an index of [0], the second has [1].
# Lists have a defined order, and that order will not change.
# Lists are changable, meaning we can add, remove items after the list is created
# Lists allow duplicates

#-------TUPLES DEFINATION-------
# Tuples are used to store multiple items under one variable.
# ( ) are used to make a tuple.
# Tuples are ordered, unchangable and allow duplicates.
# Tuples are indexed, the first item has an index [0], second has [1]
# Tuples have a defined order that will not change
# Tuples are unchangeable, we cannot add, remove items from it.
# Tuples allow duplicates

#-------SETS DEFINATION-------
# Sets are use d to store multiple items under a single variable
# { } are used to make a set.
# Sets are unordered, unchangable, unindexed and dont allow duplicates
# Sets do not have a defined order, they can appear in diffrent order every time you use them.
# Set items cannot be changed once the set is created 
# Sets do not allow duplicates

#-------DICTIONARIES DEFINATION-------
# Dictionaries are used to store key:value pairs.
# {key : value} are used to make a dictionary.
# Dictionary items are ordered, changeable, and does not allow duplicates.


# ------------LIST------------
courses = ["English", "History", "Maths", "Comp Sci"]
# list indexes start with 0

# Engilsh   [0]
# History   [1]
# Maths     [2]
# Comp Sci  [3]

print(courses)  # ['English', 'History', 'Maths', 'Comp Sci']
print(len(courses))    # 4

print(courses[3])   # Comp Sci
print(courses[-2])  # Maths --from end

print(courses[0:2])  # ['English', 'History']

# ------------ADDING ITEMS TO LIST------------
courses.append("Art")
print(courses)      # ['English', 'History', 'Maths', 'Comp Sci', 'Art']

courses.insert(2, "Physics")
print(courses)  # ['English', 'History', 'Physics', 'Maths', 'Comp Sci', 'Art']

# ------------COMBINING 2 LISTS------------
courses2 = ['Social Studies', 'Geography']

courses.extend(courses2)
# ['English', 'History', 'Physics', 'Maths', 'Comp Sci', 'Art', 'Social Studies', 'Geography']
print(courses)

# ------------REMOVING ITEMS FROM LIST------------
courses.remove("Maths")
# ['English', 'History', 'Physics', 'Comp Sci', 'Art', 'Social Studies', 'Geography']
print(courses)

courses.pop()
# ['English', 'History', 'Physics', 'Comp Sci', 'Art', 'Social Studies']
print(courses)

# ------------SORTING A LIST-----------
courses.sort()
# ['Art', 'Comp Sci', 'English', 'History', 'Physics', 'Social Studies']
print(courses)

courses.sort(reverse=True)
# ['Social Studies', 'Physics', 'History', 'English', 'Comp Sci', 'Art']
print(courses)

sorted_courses = sorted(courses)
#['Art', 'Comp Sci', 'English', 'History', 'Physics', 'Social Studies']
print(sorted_courses)

nums = [1, 5, 2, 6, 3, 1]
print(min(nums))    # 1
print(max(nums))    # 6

sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 1, 2, 3, 5, 6]

print(sum(nums))    # 18

# -----------FINDING A VALUE-----------
print(courses.index("Comp Sci"))  # 4

print("Art" in courses)  # True

for item in courses:
    print(item)

# ------------EMPYT LIST------------
emptyList=[]
#or
emptyList=list()

# -----------TUPLE-----------
# Tuples use "()" instead of "[]"
# Tuples are Immutable(Cant modify)

tuple_1 = ("Math", "Sci", "Physics", "Geography")
print(tuple_1)
# tuple_1[1] = "Art"    # Cannot be done
# ------------EMPTY TUPLE------------
emptyTuple=()
#or
emptyTuple=tuple()

# -----------SETS-----------
set_1 = {"Math", "Sci", "Physics", "Geography"}
set_2 = {"Math", "Design", "Physics", "Art"}
print(set_1.intersection(set_2))  # {'Physics', 'Math'}
print(set_1.difference(set_2))  # {'Geography', 'Sci'}
print(set_1.union(set_2))   # {'Geography', 'Math', 'Physics', 'Sci', 'Art', 'Design'}
# ------------EMPTY SET------------
emptySet=set()

# -----------CONCLUSION-----------
# Lists use []
# Tuples use ()
# Sets use {}
# If you need something that you can modify then use a list
# If you need something the use a tuple

