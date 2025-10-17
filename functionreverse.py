
def read():
    return int(input("enter a number"))
    
def rev(num):
    revs=0
    while num!=0:
        digit=num % 10
        revs=revs*10+digit
        num=num//10
    print("reversed number is ",revs)
num=read()
rev(num)
