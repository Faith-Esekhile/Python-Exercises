seconds=int(input("enter  number of seconds :"))
if seconds >= 60 and seconds < 3600:
    if seconds % 60 != 0:
        print((seconds//60),"minutes.",seconds %60,"seconds")
    else:print(seconds//60,"minute")
if seconds >= 3600  and seconds < 86400:
    if seconds %  3600 != 0:
        print(seconds//3600,"hours",(seconds%3600)//60,"minutes",(seconds%3600)%60,"seconds")
    else:print(seconds/3600,"hour")
if seconds  >= 86400:
    if seconds % 86400 !=0:
        print(seconds//86400,"days",(seconds%86400)//3600,"hours",((seconds%86400)%3600)//60,"minutes",((seconds%86400)%3600)%60,"seconds")
    else:print(seconds/86400,"day")
else:
    print("")