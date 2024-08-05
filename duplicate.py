a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
if (a == b and a == c):
    print(a)
elif (a == b or a == c):
    print(b+c)
elif(b == c or b == a):
    print(a+c)
elif(c == b or c == a):
    print(a+b)
else:
    print(a+b+c)
