print("reboot the computer and try to connect and answer yes or no")
answer=str(input("did that fix the problem :"))
if answer == "no":
    print("reboot the computer and try to connect ")
    answer=str(input("did that fix the problem:"))
if answer == "no":
    print("Make sure the cables between the router and modem are plugged in firmly")
    answer=str(input("did that fix the problem :"))
if answer == "no":
    print("move the router to a new location ") 
    answer=str(input("did that fix the problem : "))
if  answer == "no":
    print("get a new router")  
else:
    print("")   