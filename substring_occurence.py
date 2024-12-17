st = str(input("Enter a string : "))
sub_st = str(input("Enter the substring : "))
count = 0
len_st = len(st)
len_sub_st = len(sub_st)
for i in range(0,len_st):
    if( st[i] == sub_st[0] ):
        m,n = i,0
        flag = 0
        while(m<len_st and n<len_sub_st):
            if( st[m] == sub_st[n] ):
                m = m + 1
                n = n + 1
            else:
                flag = 1
                break
        if( flag == 0 and n == len_sub_st ):
            count = count + 1
        if (count == 1):
            print("The first occurence is",i+1)
