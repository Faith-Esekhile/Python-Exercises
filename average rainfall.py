years=int(input("enter number of years:"))
for x in range (1,years+1):
    print("for year",x)
    total=0
    totalmonth=0
    for m in range(1,13):
        print("month ",m)
        month=int(input("enter the rainfall inch:"))
        total=total+month
        average=total/m
        if month != 0:
            for t in range (month):
                totalmonth=month
print("the total number of month is",totalmonth)
print("the total inches of rainfall is",total)
print("the average number of rain fall in",years,"years is",average)
    
   
