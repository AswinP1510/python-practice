n = int(input("Enter a number : "))
res = 1
for i in range (2,n):
    if ( n % i == 0):
        res = 0
if( res == 0):
    print("Not prime")
else:
    print("Prime")
