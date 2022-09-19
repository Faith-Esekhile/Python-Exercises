organ=int(input("enter Starting number of organisms: "))
increase=int(input("enter Average daily increase: "))
multiply=int(input("enter number of days to multiply:"))
print("day \t population")
total=organ
print("1\t",organ)
for x in range(2,multiply+1):
    percent=increase/100
    sum=total*percent
    total=total+sum
    print(x,"\t",format(total,".3f"))
