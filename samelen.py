a=[1,2,3,4]
b=[5,8,3,4]

if(len(a)==len(b)):
   print("same length",len(a),"and ",len(b))
else:
    print("not same length")

if(sum(a)==sum(b)):
    print("same sum, sum= ",sum(a))
else:
    print("sum is not same sum of a = ",sum(a),"sum of b = ",sum(b))

for i in a:
   for j in b:
      if i==j:
         print("repeated ",i,j)
                                    
