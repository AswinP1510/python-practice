n = int(input("Enter a number : "))
r = 0
x = 0
v = n
while n > 0:
    r = n % 10
    n = n // 10
    x = x*10 + r
if ( x == v ):
    print("Palindrome",x)
else:
    print("Not Palindrome")

