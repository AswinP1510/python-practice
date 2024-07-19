'''
Q3. Write a program named expression_01 to take x,y,z as input as print the value of the given expression 4x^4 + 3y^3 + 2z + 1
'''

x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))
z = int(input("Enter the value of z : "))

exp1 = ( 4 * x * x * x * x ) + ( 3 * y * y * y ) + ( 2 * z ) + 1

print(exp1)