'''
n = int(input("Enter the rows : "))
m = int(input("Enter the column : "))
l = []
p = []

for i in range(0,n):
    for j in range(0,m):
        x = int(input(f"Enter {i},{j} : "))
        l.append(x)
    p.append(l)
    l = []
print(p)
''' 

a = 0
b = 0
l = [[2,3,4],[5,7,6]]
n = len(l)
m = len(l[0])
z = l[0][0]
for i in range(0,n):
    for j in range(0,m):
        print(i,j)
        if( l[i][j] > z ):
            z = l[i][j]
            a = i
            b = j
print("The postiion : ",a,b)

'''
n = eval(input("Enter a list : "))
x = n[0]
y = 0
for i in range(0,len(n)):
    if( n[i] >= x ):
        x = n[i]
        y = i
print("The max number is : ",x)
print("The position of that element : ",y)
print(n)
'''
