n = int(input("Enter a number : "))
r = 0
x = n*n
res = 0
while x > 0:
    r = x % 10
    x = x // 10
    res = res + r
if ( res == n ):
    print("Neon",n)
else:
    print("Not Neon")
