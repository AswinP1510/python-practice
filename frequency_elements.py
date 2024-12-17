l = eval(input("Enter a list : "))
k = l
count = 1
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if( l[i] == l[j] and i != j and l[i] != -1 and l[j] != -1 ):
            count = count + 1
            l[j] = -1
    if( l[i] != -1 ):
        print("The element",l[i],"is repeating",count,"times")
        count = 1
