n = [5,9,6,8,7]
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if ( n[j] < n[i] ):
            c = n[i]
            n[i] = n[j]
            n[j] = c
print(n)

        
    
