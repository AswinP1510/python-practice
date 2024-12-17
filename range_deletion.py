'''
WAP to delete a given range of values specified by the users
EX : [1,2,3,4,5]
    lower bound = 1
    upper bound = 3
Output : [1,5]
'''

'''
n = eval(input("Enter a list : "))
l = int(input("Enter the lower bound : "))
u = int(input("Enter the upper bound : "))
if ( len(n) < l or len(n) < u):
    print("")
else:
    for i in range(l,u+1):
        n.pop(l)
        print(i)
print(n)
'''
n = eval(input("Enter a list : "))
l = int(input("Enter the lower bound : "))
u = int(input("Enter the upper bound : "))
del n[l:u+1]
print(n)
