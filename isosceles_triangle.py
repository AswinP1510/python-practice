n = int(input("Enter a number : "))
for i in range(0,n):
    for j in range(n-i-1,0,-1):
        print(" ",end="")
    for k in range(0,i+1):
        print("* ",end="")
    print()
