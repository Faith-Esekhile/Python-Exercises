day=int(input("enter the numbers of days worked :"))
print("day\t  pennies")
for x  in  range(1,day+1):
    total=0
    for c in range(1,x+1):
        total=total+c
    print (x,'\t',c )
dollar =(total/100)
print("your total pay in pennies is",total)
print("you have earned $",dollar)

        

   

    
