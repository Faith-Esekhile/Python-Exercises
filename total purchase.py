item1= int(input("enter price of first item purchased:"))
item2=int(input("enter price of second item purchased:"))
item3=int(input("enter price of third item purchased"))
item4=int(input("enter price of fourth item purchased"))
item5=int(input("enter price of fifth item purchased"))
total=item1+item2+item3+item4+item5
print("your total amount of purchase is",total)
tax=0.07*total
print("your tax sale is", tax)
total_sales=tax+total
print("your total sales is =" ,total_sales)

