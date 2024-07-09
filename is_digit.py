'''
ASCII Values 
============

0 - 9 -> 48-57
a - z -> 65-90
A - Z -> 95-122


Q2. Write a program named is_digit.py to find out whether a character entered by the user is a digit or not.
'''

n = input("Enter a number : ")

asc_n = ord(n)

if((asc_n >= 65 and asc_n <= 90) or (asc_n >= 95 and asc_n <= 122)):
    print("Not a digit")
elif(asc_n >= 48 and asc_n <= 57):
    print("Is a digit")
else:
    print("Neither a character or digit")