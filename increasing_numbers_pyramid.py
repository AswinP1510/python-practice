n = int(input("Enter a number : "))
k = 0
for i in range (1,n+1):
    for j in range (1,i+1):
        k = k + 1
        print(k,end=" ")
    print("\n",end="")
