a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
hcf1 = 0
hcf2 = 0
for i in range(1,a+1):
    if ( a % i == 0 and b % i == 0 ):
        hcf1 = i
print(hcf1)
