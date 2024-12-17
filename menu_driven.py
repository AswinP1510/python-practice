while True:
    print("Enter 1 for prime")
    print("Enter 2 for reverse digit")
    print("Enter 3 for exit")
    ch = int(input("Enter your choice : "))
    v = 0
    if ch == 1:
        count = 0
        n = int(input("Enter a number : "))
        for i in range(2,n-1):
            if ( i % n == 0 ):
                count = 1
        if( count == 0 ):
            print("Prime",n)
        else:
            print("Not Prime")
    elif ch == 2:
        n = int(input("Enter a number : "))
        while n > 0:
            r = n % 10
            n = n // 10
            v = v*10 + r 
        print(v)
    elif ch == 3:
        print("Thank You")
        break
    else:
        print("Wrong input")
    
        
