'''
st = str(input("Enter something : "))
if( st == st[::-1] ):
    print("Palindrome",st)
else:
    print("Not Palindrome")
'''
st = str(input("Enter something : "))
l = len(st)//2
k = len(st)-1
flag = 0
for i in range(0,l):
    if(st[i] != st[k-i]):
        flag = flag + 1
        break

if( count == 0):
    print("Palindrome",st)
else:
    print("Not Palindrome")
    
            
            
    
    
