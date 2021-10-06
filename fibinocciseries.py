def fib(n,p):
    a,b=0,1
    if n<0 or p<0:
        print("invalid")
    else:
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2,n):
                c=a+b
                a=b
                b=c
                if c>p:
                    break
                print(c)
       ### Fibinocci series
