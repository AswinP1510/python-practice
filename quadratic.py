a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
d = (b**2-(4*a*c))
x1 = (-b+(d**0.5))/2*a
x2 = (-b-(d**0.5))/2*a
if ( a==0 ):
    print("Quadratic equations conditions not satisfied")
else:
    if( d>0 ):
        print("The roots are real and unnequal")
    elif( d==0 ):
        print("The roots are real and equal")
    elif( d<0 ):
        print("The roots are imaginary")
    print("The roots are : ",x1,x2)
