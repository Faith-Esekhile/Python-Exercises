sales=float(input("enter total sales of the month:"))
state=sales/0.05
country=sales*0.025
total=country+state
print("The amount of county sales tax is ", format(country,".2f"))
print("the amount of state sales tax is",format(sales,".2f"))
print("The total sales tax (county plus state) is",total)

