n = int(input("Enter a number : "))
for i in range(0,n):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(0,i+1):
        if( i == j or j == 0 ):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
for i in range(1,n):
    for k in range(0,i+1):
        print(" ",end="")
    for j in range(n-1,i-1,-1):
        if( i == j or j == (n-1) ):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
