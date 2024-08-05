#In the range 1 to n , print all the numbers divisible by m.
n = int(input("Enter a number : "))
m = int(input("Enter a number : "))
for i in range(1,n+1):
    if(i % m == 0):
        print(i)
