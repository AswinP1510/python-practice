t = eval(input("Enter a tuple : "))
l = list(t)
for i in range(0,len(l),2):
    if( l[i] != l[-1]):
        l[i],l[i+1] = l[i+1],l[i]
k = tuple(l)
print(k)
