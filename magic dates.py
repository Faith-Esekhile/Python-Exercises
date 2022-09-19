month = int(input("enter a month in numeric form"))
day=int(input("enter a day in numeric form"))
if month == 2 and day >29:
    print("february ends at day 29 do not enter year")
    34
year=int(input("enter a two digit year"))
if( month >=1 and month <=12) and (day >= 1 and day <= 31):
   
    if month*day == year:
        print("the date is magic")
    else:
        print("the date is not magic")
else:
    print ("please enter the correct day of the year or month of the year")

