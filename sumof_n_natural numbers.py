'''
WAP to calculate the sum of n natural numbers where n will be provided by the user.
'''

'''using for loop'''
'''
n = int(input("Enter a number : "))
res = 0
for i in range(0,n):
    x = int(input("Enter the number to be calculated : "))
    res = res + x
print("The sum of numbers is : ",res)
'''
n = int(input("Enter a number : "))
s = (n*(n+1))/2
print("Sum : ",s)
