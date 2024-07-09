'''
Q2. Write a program named temperature_average to take the temparature of 7 days of a week in celcius, compute the average temparature and print hot if the temperature is above 40 degrees, otherwise print cool.
'''

day1 = int(input("Enter temperature of day 1 in celcius: "))
day2 = int(input("Enter temperature of day 2 in celcius: "))
day3 = int(input("Enter temperature of day 3 in celcius: "))
day4 = int(input("Enter temperature of day 4 in celcius: "))
day5 = int(input("Enter temperature of day 5 in celcius: "))
day6 = int(input("Enter temperature of day 6 in celcius: "))
day7 = int(input("Enter temperature of day 7 in celcius: "))

avg_temp = ( day1 + day2 + day3 + day4 + day5 + day6 + day7 ) // 7

if (avg_temp >= 40):
    print("hot",avg_temp)
else:
    print("cold",avg_temp)



