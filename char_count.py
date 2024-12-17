st = input("Enter a string : ")
str_list = st.split(" ")
sub_st = input("Enter a sub string : ")
count = 0
for i in range(0,len(str_list)):
    if( sub_st == str_list[i] ):
        count = count + 1
print(count)
