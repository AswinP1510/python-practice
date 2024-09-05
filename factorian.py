def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res

m = int(input("Enter a number : "))
r = 0
sum = 0
x = m
while( x > 0 ):
    r = x % 10
    x = x // 10
    sum = sum + factorial(r)
if( sum == m ):
    print("Factorian")
else:
    print("Not factorian")
    
