n = int(input("Enter a number : "))
for i in range(0,n):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(0,i+1):
        if( i == 0 or i == (n-1)):
            print("* ",end="")
        else:
            if( j == 0 ):
                print("* ",end="")
            elif( j == i ):
                print("* ",end="")
            else:
                print("  ",end="")
    print()
