std={"name":"john","roll_no":"1","reg no":"100","dep":"mca","sem":"1"}
std["total_mark"]=87
print(std)
total_mark=std["total_mark"]
if(total_mark>=90):
     grade="A grade"
elif(total_mark>=82):
    grade="B grade"
elif(total_mark>=75):
    grade="c grade"
elif(total_mark>=60):
    grade="D grade"
elif(total_mark>=50):
    grade="P grade"
else:
    grade="Fail"

std["grade"]=grade
del std["roll_no"]
print(std)
     
