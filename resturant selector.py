vegetarian=str(input("is anyone at your party vegetarian:"))
vegan=str(input("is anyone at your party vegan:"))
gluten_free=str(input("is any one at your party gluten-free:"))

if vegetarian == "yes" and vegan == "yes" and gluten_free =="yes":
    print("your choices are :\n corner cafe \n the chef kitchen")
elif vegetarian ==  "yes" and vegan == "yes" and gluten_free == "no":
    print("here are your choices:")
    print("the chef kitchen")
    print("corner cafe")
elif vegetarian == "yes"   and vegan == "no" and gluten_free== "yes":
    print("here are your choices:\n main street pizza company\n corner cafe\n the chef kitchen ")
elif vegetarian == "no"   and vegan == "yes" and gluten_free== "yes":
    print("here are your choices:\n corner cafe \n the chef kitchen ")
elif vegetarian == "no"   and vegan == "no" and gluten_free == "yes":
    print("here are your choices:\n corner cafe \n the chef kitchen\nmain street pizza company ")
elif vegetarian == "no"   and vegan == "yes" and gluten_free == "no":
    print("here are your choices:\n corner cafe \n the chef kitchen\n")
elif vegetarian == "yes"   and vegan == "no" and gluten_free == "no":
        print("here are your choices:\n corner cafe \n the chef kitchen\n main street pizza company\n mama italian fine kitchen")
elif vegetarian == "no" and vegan == "no" and gluten_free =="no":
    print(" your choice is \n joe's gourmet burgers")
else:
    print("invalid answer")





    
    

    