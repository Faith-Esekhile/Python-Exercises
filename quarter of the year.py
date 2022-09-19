month=int(input("enter the number of the month of the year"))
if month <=12 and month  >=1 :
    if  month >=1 and  month<=3 :
        print("the month is in the first quarter")
    elif month >=4 and month<=6:
        print("the month is in the second quarter")
    elif month >=7 and month<=9:
        print("the month is in the third quarter")
    elif month >=10 and month<=12:
        print("month is in the fourth quarter")
else:
    print("invalid number")