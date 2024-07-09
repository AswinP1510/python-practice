'''
Write a program to swap the values of 3 numbers such that
I. the value of first value becomes equal to the second value
II. the value of second value becomes equal to the third value
III. the value of third value becomes equal to the first value
'''
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
d = a + b + c
a = d - (a+c)
c = d - (b+c)
b = d - (c+b)
print("A : ",a)
print("B : ",b)
print("C : ",c)
