integer=int(input("enter an integer"))
if integer > 0  :
    if integer % 2 == 0 :
        print("even")
    else :
        print("odd")
    print("positive")
elif integer <0:
    print("negative")
elif integer  == 0:
    print("zero")
else:
    print("invalid")
