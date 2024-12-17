st = input("Enter a string : ")
alpha = 0
digit = 0
schar = 0
for i in st:
    if( i.isalpha() == True ):
        alpha = alpha + 1
    elif( i.isdigit() == True ):
        digit = digit + 1
    else:
        schar = schar + 1
print("Alphabet : ",alpha)
print("Digit : ",digit)
print("Special char :",schar)
        
        
