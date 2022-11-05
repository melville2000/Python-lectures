num = 3.1

print(type(num))
# to find the type of numeric data in the variable num

# ------------ARETHMETHIC OPERATORS------------
# Addition:           3 + 2     5
# Substraction:       3 - 2     1
# Multiplaication:    3 * 2     6
# Division:           3 / 2     1.5
# Floor Division:     3 // 2    1
# Exponent:           3 ** 2    9
# Modulus:            3 % 2     1

print(3 % 2)
# Incrementing values
num = 1
num += 1
print(num)  # 2

# aboslute value
print(abs(-3))  # 3  removes negative sign

# round
print(round(3.75))  # 4 Rounds off whole number
print(round(6.23, 1))  # 6.2 Rounds of decimal

# ------------COMPARISON OPERATORS------------
# Equal:                ==
# Not Equals:           !=
# Greater Than:         > 
# Less Than:            < 
# Greater or Equal:     >=
# Greater or Equal:     <=
# Object Identity:      is

# casting values from stirng to intiger
num1 = "100"
num2 = "200"
print(num1+num2)  # 100200
# ----------------------------------
num1 = int("100")
num2 = int("200")
print(num1+num2)  # 300
