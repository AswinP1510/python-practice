p = [1,2,2,3,4,4,5,6,7,8]
q = [2,4,5,6,7]
k = []
i = 0
j = 0
while(i < len(p) and j < len(q)):
    if ( p[i] < q[j] ):
        k.append(p[i])
        i = i + 1
    else:
        k.append(q[j])
        j = j + 1
while(i < len(p) ):
    k.append(p[i])
    i = i + 1
while(j < len(q) ):
    k.append(q[j])
    j = j + 1
print(k)
