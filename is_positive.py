'''
Q3.  Write a program named is_positive.py to find out whether an integer number entered by the user is positive, negative or zero.
'''

n = int(input("Enter a number : "))

if ( n > 0 ):
    print("Positive Integer")
elif( n < 0 ):
    print("Negative Integer")
else:
    print("The number is 0")