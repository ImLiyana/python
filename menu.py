print("1.occurance of word")
print("2.frequency of words")
print("3.factorial")
print("4.Exit")
choice=int(input("Enter Your Choice"))
if(choice==1):
           a=input("Enter a sentance")
           b=a.split()
           for i in b:
               print(i,b.count(i))
if(choice==2):
    a=input("Enter a word")
    for i in a:
       print( i,a.count(i))

if(choice==3):
    a=int(input("Enter a number"))
    fact=1
    for i in range(a,0,-1):
        fact=fact*i
    print(fact)
if(choice==4):
    print("end")
    
                
    
    
    
      

    
