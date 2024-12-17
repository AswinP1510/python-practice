n = int(input("Enter a number : "))
x = n
r = 0
v = 0
while True:
    while n > 0:
        r = n % 10
        n = n // 10
        v = v + r
    if( v <= 9 and v != 1 ):
        print("Not Magic")
        break
    if( v == 1 ):
        print("Magic",x)
        break
    else:
        n = v
        r = 0
        v = 0
