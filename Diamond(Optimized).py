n = int(input("Enter a number : "))
a = n-1
b = n-1
x = 1
y = 1
for i in range(0,n):
    print(" "*a+"* "*x)
    a = a - 1
    x = x + 1
for j in range(0,n):
    print(" "*y+"* "*b)
    b = b - 1
    y = y + 1
        
        
