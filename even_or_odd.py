n = int(input("Enter a number : "))
r = 0
x = 0
v = 1
if ( n % 2 == 0):
    while n > 0:
        r = n % 10
        n = n // 10
        x = x + r
    print(x)
else:
    while n > 0:
        r = n % 10
        n = n // 10
        v = v * r
    print(v)
