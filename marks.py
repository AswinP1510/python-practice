'''
91-100 = A+
90-81 = A
80-71 = B
70-61 = C
60-51 = D
50-41 =E
0-40 = F
'''

n = int(input("Enter your marks : ")) # n is storing the user's marks

if(n >= 91 and n <=100):
    print("Your grade is A+")
elif(n <= 90 and n >= 81):
    print("Your grade is A")
elif(n <= 80 and n >= 71):
    print("Your grade is B")
elif(n <= 70 and n >= 61):
    print("Your grade is C")
elif(n <= 60 and n >= 51):
    print("Your grade is D")
elif(n <= 50 and n >= 41):
    print("Your grade is E")
elif(n <= 40 and n >= 0):
    print("You have failed")
else:
    print("There is a mistake in entering the marks")