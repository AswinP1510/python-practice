n = int(input("Enter a number : "))
var = 0
for i in range(2,n-1):
    if( n % i == 0 ):
        var = 1
if( var == 0 ):
    print("Prime")
else:
    print("Not prime")
