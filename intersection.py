n = [7,8,3,5,6]
m = [7,3,6,4,9]
l = []
el = 0
for i in range(0,len(n)):
    for j in range(0,len(m)):
        if( n[i] == m[j]):
            el == n[i]
            if el not in l:
                l.append(n[i])
print(l)
