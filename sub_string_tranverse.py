st = input("Enter string : ")
sub_st = input("Enter sub-string : ")
len_st = len(st)
len_sub_st = len(sub_st)
count = 0
for i in range(0,len_st):
    if(st[i] == sub_st[0]):
        x,y = i,0
        flag = 0
        while(x<len_st and y<len_sub_st):
            if(st[x] == sub_st[y]):
                x = x + 1
                y = y + 1
            else:
                flag = 1
        if( flag == 0 and y == len_sub_st ):
            count = count + 1
    flag = 0
    x = 0
    y = 0
print(count)
