n = eval(input("Enter a list : "))
res = 0
for i in range(len(n)):
    res = res + n[i]
avg = res/len(n)
print("The average is : ",avg)
