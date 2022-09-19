mass=int(input("enter the mass of the object"))
weight = mass*9.8
if weight > 500:
    print("the object is too heavy")
elif weight < 100:
    print("the object is too light")
else:
    print("invalid number")