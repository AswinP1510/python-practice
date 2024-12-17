t = eval(input("Enter a tuple : "))
l = list(t)
k = l
count = 0
res = 0
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if ( l[i] == l[j] and l[i] != -1 and i != j):
            count = count + 1
            l[j] = -1
    if( count >= 1):
        res = res + 1
    count = 0
m = tuple(k)
print("Number of duplicate items : ",res)
print(k)
            
            
