days = int(input("Enter number of days : "))
year = days // 365
days = days % 365
weeks = days // 7
days = days % 7
print(year,"Years",weeks,"weeks",days,"days")
