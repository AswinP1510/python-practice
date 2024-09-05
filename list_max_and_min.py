n = eval(input("Enter a list : "))
if( len(n) == 0):
    print("Error")
else:
    res = n[0]
    lst = n[0]
    for i in range(len(n)):
        if( n[i] > res ):
            res = n[i]
        if( n[i] < lst ):
            lst = n[i]
    print("Max :",res)
    print("Min :",lst)
