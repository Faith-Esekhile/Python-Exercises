food=int(input("enter food charge ="))
tip= 0.18*food
tax= int(0.07*food)
total=food+tip+tax
print("your tip payment is =",tip)
print("your tax payment is =",tax)
print("your total is =",total)