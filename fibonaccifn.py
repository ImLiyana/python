n=int(input("enter a number"))
def fibonacci(n):
    if n==1:
        return 1
    n1,n2=0,1
    print(n1)
    print(n2)
    for i in range(2,n):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
fibonacci(n)

        
        
