weight=int(input("enter weight in pounds:"))
height=int(input("enter height in inches:"))
bodymass=weight*(703/(height**2))
if bodymass >=18.5 and bodymass <= 25:
    print("you have an optimal weight")
elif bodymass > 25:
    print("you are over weight")
elif bodymass < 18.5:
    print("you are over weight")
else:
    print("enter valid number")