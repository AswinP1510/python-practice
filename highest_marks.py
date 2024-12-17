n = eval(input("Enter the names : "))
m = eval(input("Enter the marks : "))
x = 0
for i in range(0,len(m)):
    if ( m[i] > m[x] ):
        x = i
print(n[x],"Scored",m[x])
