square_feet=112
gallon=1
labour=8
wall=float(input("enter the square feet of wall to be painted:"))
price =float(input("enter price of paint per gallon:"))
paint=wall/square_feet
hours=paint*labour
paint_cost=paint*price
labour_charge=hours*35
total=labour_charge+paint_cost
print("The number of gallons of paint required is",format(paint,".2f"))
print("The hours of labor required is",format(hours,".2f"))
print("The cost of the paint is",format(paint_cost,".2f"))
print("The labor charges is",format(labour_charge,".2f"))
print("The total cost of the paint job is",format(total,".2f"))


