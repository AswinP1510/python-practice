a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
d = int(input("Enter a number : "))
if ( a<b and a<c and a<d ):
    print("a is the smallest : ",a)
elif ( b<c and b<d ):
    print("b is the smallest : ",b)
elif ( c<d ):
    print("c is the smallest : ",c)
else:
    print("d is the smallest : ",d)
