package=int(input("enter amount of package purchased:"))
if package >= 10 and package <= 19 :
    print("you have a ten percent discount")
elif package   >=20 and package <= 49 :
    print("you have a twenty percent discount")
elif package   >=50 and package <=99:
    print("your discount is 30 percent")
elif  package   >= 100:
    print("you have a 40 percent discount")
else :
    print("you have no discount")
total=package*99
print("your total amount is",total)