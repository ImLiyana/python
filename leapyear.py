cyear=int(input("Enter current year "))
finalyear=int(input("Enter final year "))
for i in range(cyear,finalyear):
    if((i%4==0)and(i%100!=0) or (i%400==0)):
        print(i)
        
    
