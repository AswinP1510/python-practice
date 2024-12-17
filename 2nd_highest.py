l = eval(input("Enter a list : "))
x = 0
y = 0
for i in range(0,len(l)):
    if ( l[i] > l[x] ):
        x = i
l.remove(l[x])
for i in range(0,len(l)):
    if ( l[i] > l[y] ):
        y = i
print(l[y])
    
        
