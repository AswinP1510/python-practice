st = str(input("Enter a string : "))
sub = str(input("Enter the substring : "))
count = 0
for i in st:
    if( st[i:i+len(sub)] == sub ):
        count = count + 1
print(count)
