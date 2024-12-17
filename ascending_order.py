l = eval(input("Enter a list : "))
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if ( l[i] < l[j] and i != j ):
            l[i],l[j] = l[j],l[i]
print(l)
