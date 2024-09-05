n = int(input("Enter a number : "))
r = 0
res = 0
while n > 0:
    r = n % 10
    n = n // 10
    res = res*10 + r
print(res)
    
