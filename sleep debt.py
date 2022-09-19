print("enter the sleeping hours for each day og the week")
total=0
for x in  range(1,8):
    hours=int(input("how many hours did you sleep "))
    if hours < 24:
        total=total+hours
        sleeptime = 56-total
        if total <= 56:
            print("really its not normal to be so hardworking")
        else:
            print("you waste time")
    else:
        print("invalid")

