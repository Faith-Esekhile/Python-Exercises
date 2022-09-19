number=int(input("enter a pocket number:"))
if number  == 0:
    print("green")
elif number  >=1 and  number <= 10:
    if number % 2 == 0:
        print("black")
    else:
        print("red")
elif number >= 11 and number  <=18:
    if  number % 2 == 0:
        print("red")
    else:
        print("black")
elif number >= 19 and number <=18:
    if number % 2 == 0:
        print("black")
    else:
        print("red")
elif number  >= 29 and number <= 36:
    if number % 2 == 0:
        print("red")
    else:
        print("black")
else:
    print("invalid number")
