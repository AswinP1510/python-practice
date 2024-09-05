a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
for j in range(a,b):
    res = 0
    r = 0
    fact = 1
    x = j
    while( x > 0 ):
        r = x % 10
        x = x // 10
        for i in range(1,r+1):
            fact = fact * i
        res = res + fact
        fact = 1
    if( j == res ):
        print("Krishnamurthy number :",res)
        
