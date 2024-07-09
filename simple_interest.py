'''
Q1. Write a program named simple_interest.py to compute the simple intrest when principle amount, time and rate of intrest are provided as inputs
'''

p = int(input("Enter the principal amount : "))
r = int(input("Enter the rate of interest : "))
t = int(input("Enter the time period : "))

interest = (p * r * t) // 100

print(interest)