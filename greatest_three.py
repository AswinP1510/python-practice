n = int(input("Enter a number : "))
m = int(input("Enter a number : "))
p = int(input("Enter a number : "))
if( n > m and n > p ):
    print("1st number is greatest",n)
elif( m > p and m > n):
    print("2nd number is greatest",m)
else:
    print("3rd number is greatest",p)
