
message = "Hello World"

print(message.lower())
# hello world
print(message.upper())
# HELLO WORLD
print(message.count("World"))
# 1 --World has repeated once
print(message.find("World"))
# 6 --World is at index 6
message = message.replace("World", "Universe")
print(message)
# hello universe

greeting = "Hello"
you = "User"
print(greeting + ", " + you + ". welcome")
#Hello, User. welcome

messageNew = '{}, {}. Welcome'.format(greeting, you)
print(messageNew)
#Hello, User. Welcome
# fstring method
messages = f'{greeting}, {you}. Welcome'
print(messages)
#Hello, User. Welcome

print(help(str))
# help
