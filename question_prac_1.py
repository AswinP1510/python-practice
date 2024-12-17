'''
m = 40
for m in range(40,10,-10):
    for i in range(5,10,3):
        print(m,i,sep='#')
'''
'''
l1 = [4,6,8]
l2 = l1*2
l3 = l2 - l1
print(l1)
'''
'''
A = 10
for S in range(0,A):
    if S % 2:
        print(S*2)
    else:
        print(S+3)
'''
'''
n = int(input("Enter a number : "))
r = 0
v = 0
a = 1
if ( n % 2 == 0 ):
    while n > 0:
        r = n % 10
        n = n // 10
        v = v + r
    print(v)
else:
    while n > 0:
        r = n % 10
        n = n // 10
        a = a * r
    print(a)
'''
n = int(input("Enter a number : "))
k = 0 
for i in range(1,n+1):
    for j in range(1,i+1):
        k = k + 1
        print(k,end=" ")
    print()  
