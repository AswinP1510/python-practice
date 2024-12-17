l = eval(input("Enter a list : "))
uni = []
for x in l:
    if x not in uni:
        uni.append(x)
    else:
        l.remove(x)
print(uni)
    
