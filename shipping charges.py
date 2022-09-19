weight=int(input("queen enter the weight of your package :"))
if weight >=1 and  weight <=2 :
    print("your shipping charge is $1.5")
elif weight >=2 and weight <=6:
    print("your shipping charge is $3.0")
elif weight >=6 and weight  <=10:
    print("your shipping charge is $4")
elif weight >= 10:
    print("your shipping charge is $4.75")
else:
    print("invalid numbers")
