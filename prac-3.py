while True:
    print("Enter 1 for area of rectangle")
    print("Enter 2 for volume of cuboid")
    print("Enter 3 for exit")
    n = int(input("Enter your choice : "))
    if n == 1:
        l = float(input("Enter length : "))
        b = float(input("Enter breadth : "))
        s = l*b
        print("Area of rectangle : ",s)
    elif n == 2:
        l = float(input("Enter length : "))
        b = float(input("Enter breadth : "))
        h = float(input("Enter height : "))
        v = l*b*h
        print("Volume of cuboid : ",v)
    elif n == 3:
        print("Thank you")
        break
    else:
        print("Incorrect Input")
    
