n=5

#*****
#*****
#*****
#*****
#*****

""" for i in range(n):
    for j in range(n):
        print("*", end="")
    print("") """
#-----------------------------------
# *****
# *   *
# *   *
# *   *
# *****
""" for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 :
            print("*", end="")
        else :
            print(" ", end = "")
    print() """
#-----------------------------------
#*
#**
#***
#****
#*****
""" for i in range(n):
    for j in range(i):
        print("*", end="")
    print()
 """
 #-----------------------------------
#*****
#****
#***
#**
#*
""" for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()
 """
#-----------------------------------
#    *
#   **
#  ***
# ****
#*****
""" for i in range(n):
    for space in range(n-i):
        print(" ", end="")
    for star in range(i):
        print("*", end="")
    print() """
#-----------------------------------
#1
#12
#123
#1234
#12345

""" for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print() """
#-----------------------------------
#12345
#1234
#123
#12
#1

""" for i in range(n):
    for j in range(1,n-i+1):
        print(j, end="")
    print() """
#-----------------------------------
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15
""" count = 0
for i in range(1,n+1):
    for j in range(i):
        count=count+1
        print(str(count) + " ", end="")
    print() """
#-----------------------------------
#1
#0 1
#1 0 1
#0 1 0 1
#0 1 0 1 0
""" count=0

for i in range(1,n+1):
    for j in range(i):
        if (i+j)%2==0:
            print("0 ",end="")
        else :
            print("1 ", end="")
    print() """
#-----------------------------------
#    *****
#   *****
#  *****
# *****
#*****

""" for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for j in range(n):
        print("*", end="")
    print() """
#-----------------------------------
#    1
#   2 2
#  3 3 3
# 4 4 4 4
#5 5 5 5 5
""" for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print(str(i)+" ", end="")
    print() """
#-----------------------------------
#        1
#      2 1 2
#    3 2 1 2 3
#  4 3 2 1 2 3 4
#5 4 3 2 1 2 3 4 5
""" 
for i in range(1,n+1):
    for j in range(n-i):
        print("  ", end="")
    for j in range(i,0,-1):
        print(str(j)+" ", end='')
    for j in range(2,i+1):
        print(str(j)+" ", end='')
    print() 
"""
#-----------------------------------
#*        *
#**      **
#***    ***
#****  ****
#**********
#**********
#****  ****
#***    ***
#**      **
#*        *
""" for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    for j in range(n-i):
        print("  ", end="")
    for j in range(i):
        print("*", end='')
    print()

for i in range(n,0,-1):
    for j in range(i):
        print("*", end='')
    for j in range(n-i):
        print("  ",end='')
    for j in range(i):
        print("*", end='')
    print() """
#-----------------------------------
#    *
#   ***
#  *****
# *******
#*********
#*********
# *******
#  *****
#   ***
#    *

""" for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*",end='')
    for j in range(i-1):
        print("*",end='')
    print() 

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*",end='')
    for j in range(i-1):
        print("*",end='')
    print() """
#-----------------------------------
#11
#122
#1233
#12344
#123455
#12344
#1233
#122
#11
""" for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        count+=1
        print(j,end="")
    print(count,end="")
    print()

for i in range(n,1,-1):
    count=0
    for j in range(1,i):
        count+=1
        print(j,end='')
    print(count,end="")
    print() """
#-----------------------------------
#*        *
#**      **
#* *    * *
#*  *  *  *
#*   **   *
#*   **   *    
#*  *  *  *
#* *    * *
#**      **
#*        * 

""" for i in range(1,n+1):
    for j in range(i):
        if j==0 or j==i-1:
            print("*", end='')
        else:
            print(" ",end='')
    for j in range((n+n)-(i+i)+1,1,-1):
        print(" ",end="")
    for j in range(i):
        if j==0 or j==i-1:
            print("*", end='')
        else:
            print(" ", end='')
    print() 
for i in range(1,n+1):
    for j in range(n):
        if j==0 or j==n-i:
            print("*", end="")
        else:
            print(" ",end='')
    for j in range(i-1):
        print(" ", end='')
    for j in range(n):
        if j==n-i or j ==0:
            print("*", end="")
        else:
            print(" ",end='')
    print()
 """
 #-----------------------------------
#    1
#   23 2
#  345 43
# 4567 654
#56789 8765
""" for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for j in range(i,i+i):
        print(j, end='')
    for j in range(i+i-2,i-1,-1):
        print(j,end='')
    print() """


for i in range(1,i<=n):
    for j in range(n-i):
        print(" ", end='')
    for j in range(i):
        print("*",end='')
    print()