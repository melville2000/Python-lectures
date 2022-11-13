# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# Logic 
# 0  +  1 =  1
# n1 + n2 = n3.....
n1=0
n2=1
n3 =0

n=100000

for i in range(n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(str(n3)+ ",", end=" ")
