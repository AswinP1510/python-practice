a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
if (a>b and a>c):
    print("A is greatest")
elif(b>c):
    print("B is greatest")
elif(c>a):
    print("C is greatest")
elif(a == b and b == c):
    print("All are equal")
