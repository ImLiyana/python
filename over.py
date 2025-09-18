b=[]
a = int(input("Enter a limit"))
for i in range(0,a):
    num=int(input("Enter number"))
    if(num>100):
            b.append("over")
    else:
            b.append(num)
    i+=1
print(b)           

