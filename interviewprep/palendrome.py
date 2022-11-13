string = 'abcdef'
list1=[]
list1[:0]= string
n=len(list1)
output=""
# for i in range(n-1,0-1,-1):
#     output += list1[i]
    
# print(output)
# if string == output:
#     print("is palendrome")
# else:
#     print("no")


print(list1[::+1])