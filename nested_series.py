n = int(input("Enter a number : "))
res = 0
for i in range(1,n+1):
    for j in range(i,n+1):
        res = res + i
print("The sum is :",res)
