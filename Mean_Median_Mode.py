n = eval(input("Enter a list : "))
res = 0
l = 0
mode = 0
med1 = (len(n)-1)/2
med2 = (len(n)+1)/2
med1 = int(med1)
med2 = int(med2)
for i in range(len(n)):
    res = res + n[i]
    if( n[i] > mode ):
        mode = n[i]
print("The mode is",mode)
avg = res/len(n)
if( len(n) % 2 != 0 ):
    print("The median is : ",n[med1])
else:
    print("The median is : ",(n[med1]+n[med2])/2)
print("The mean is : ",avg)
