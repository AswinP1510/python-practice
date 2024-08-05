n = int(input("Enter 1 for cirlce and 2 for square : "))
if(n == 1):
    r = int(input("Enter the radius : "))
    ar = 3.14*r*r
    print("Area : ",ar)
elif(n == 2):
    s = int(input("Enter the side : "))
    area = s*s
    print("Area : ",area)
else:
    print("Incorrect input")
