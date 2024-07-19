'''
Q7. Write a program named greater_two.py to accept two numbers from the user and print the greater number. If both the 
numbers are equal print relavant message.
'''
A = int(input("Enter the first number : "))
B = int(input("Enter the second number : "))

if (A > B):
    print("A is greater than B")
elif (B > A):
    print("B is greater than A")
else:
    print("Both are equal")