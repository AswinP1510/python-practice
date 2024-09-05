n = int(input("Enter the limit of fibonacci series : "))
a = 0
b = 1
print(0)
print(1)
for i in range(0,n):
    c = a + b
    a = b
    b = c 
    print(c)
