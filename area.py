'''
Q5. Write a menu-driven program named area.py to find the area of a circle, rectangle or square based on the input given by the user. Consider pi = 3.14
'''

print("1. Circle\n2. Square\n3. Rectangle\nEnter your Choice:", end="")
ch = int(input())

if ch == 1:
    r = int(input("Enter radius : "))
    area = 3.14 * r * r
    print(area)
elif ch == 2:
    s = int(input("Enter the side of square :"))
    s_area = s * s
    print(s_area)
elif ch == 3:
    l = int(input("Enter the length : "))
    b = int(input("Enter the breadth : "))
    r_area = l * b
    print(r_area)
else:
    print("Invalid Input!")

