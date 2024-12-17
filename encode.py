ch = input("Enter a word : ")
st = ""
for i in ch:
    x = ord(i)
    l = ""
    k = ""
    if ( x >= 65 and x <= 90 ):
        y = x - 65
        y = (y + 3) % 26
        x = y + 65
        k = chr(x)
    elif( x >= 97 and x <= 122 ):
        z = x - 97
        z = (z + 3) % 26
        x = z + 97
        l = chr(x)
    st = st + k + l
    x = ""
print(st)
