n = int(input("Enter a number : "))
for i in range(0,n):
    for k in range(0,i):
        print(" ",end="")
    for j in range(i+1,n+1):
        print(j,end=" ")
    print()
        
