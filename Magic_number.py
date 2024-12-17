n = int(input("Enter a number : "))
x = n
r = 0
v = 0
res = 0
a = 1
while a > 0: 
    if( v == 1 ):
        print("Magic Number : ",x)
        a = 0 
    elif( v <= 9 and v != 1 and v != 0):
        print("Not Magic Number")
        a = 0
    elif( v >= 10 ):
        n = v
        v = 0
        r = 0
        while n > 0:
            r = n % 10
            n = n // 10
            v = v + r  
    else:
        while n > 0:
            r = n % 10
            n = n // 10
            v = v + r
        
    
