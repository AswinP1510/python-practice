'''
Q8. Write a program named greater_three.py to accept three numbers from the user and print the greater number. 
If all are equal print relavant message to the user.
'''
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))

if (a>b and a>c):
    print("A is the greatest")
elif (b>a and b>c):
    print("B is the greatest")
elif (c>a and c>b):
    print("C is the greatest")
else:
    print("All are equal")