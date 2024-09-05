n = int(input("Enter a number : "))
l = []
count = 0
for i in range(0,n):
    x = int(input("Enter the number : "))
    l.append(x)
for j in range(len(l)):
    if ( l[j] % 7 == 0 and l[j] % 2 != 0):
        print(l[j])
        count = count + 1
print("The total numbers are :",count)

