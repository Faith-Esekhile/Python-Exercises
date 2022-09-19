pennies=int(input("enter number of pennies :"))
nickles=int(input("enter number of nickles:"))
dimes=int(input("enter number of dimes:"))
quarter=int(input("enter number of quarter:"))
p=pennies/100
n=nickles/20
d=dimes/10
q=quarter/4
dollar=p+n+d+q
if pennies and nickles and dimes and quarter < 0:
    print("enter correct amount of money")
elif dollar == 1:
     print("you have won the game")
elif dollar > 1:
    print("amount entered was more than one dollar")
else:
    print("the amount entered  was less than one dollar")

       

