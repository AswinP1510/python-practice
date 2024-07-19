'''
What are conditional statements?
==================================
Performing a task (Executing a block of code) on basis of a given condition

For Example!

If you have 20Rs,
    Buy Choclates
Else,
    Dont Buy Choclates
    

Conditional Statements in Python
=================================
    if
    if-else
    if-elif
    if-elif-else
    
Syntax
===========

if (condition):
    // code

elif (condition):
    // code

else:
    //code

Q6. Write a code named vote.py to check whether a person is eligable to vote or not, take age as input and consider 18 as 
legal voting age.
'''
age = int(input("Enter your age : "))

if (age >= 18):
    print("You are eligible to vote")
else :
    print("You are not eligible to vote")