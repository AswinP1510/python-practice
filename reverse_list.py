t = eval(input("Enter a list : "))
l = []
for i in range(len(t)-1,-1,-1):
    l.append(t[i])
tup = tuple(l)
print(tup)
