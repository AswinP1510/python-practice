amt = int(input("Enter the amount : "))
fivehun = amt // 500
amt = amt % 500
twohun = amt // 200
amt = amt % 200
onehun = amt // 100
amt = amt % 100
fifty = amt // 50
amt = amt % 50
twenty = amt // 20
amt = amt % 20
ten = amt // 10
amt = amt % 10
five = amt // 5
amt = amt % 5
one = amt
print(fivehun,"Five hundreds",twohun,"Two hundreds",onehun,"One hundreds",fifty,"Fifty",twenty,"Twenty",ten,"Ten",five,"Five",one,"One")
