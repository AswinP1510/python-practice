'''
Operators in Python
======================

Types of Operators:
    Arithmatic Operators
    Relational Operators
    
Artihmatic Operators
======================
    + -> Sum
    - -> Difference/Substraction
    * -> Product/Multiplication
    / -> Division/Quotient
    % -> Remainder/Modulus
    // -> Whole Division
'''

'''
Q1. Write a program named calculator.py to compute the following for two given numbers:

i. Sum
ii. Difference
iii. Product
iv. Quotient
v. Modulus

The numbers are to be given as user input.
'''

a = int(input("Enter A:"))
b = int(input("Enter B:"))

sum = a + b
diff = a - b
prod = a * b
quot = a / b
mod = a % b

print(sum)
print(diff)
print(prod)
print(quot)
print(mod)