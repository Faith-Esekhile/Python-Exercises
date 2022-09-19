speed=int(input("what is the speed of your vehicle in mph:"))
hours=int(input("how many hours has it traveled:"))
print("hours \t distance traveled")
for x in range (1,hours+1):
    distance=speed*x
    print(x,"\t",distance)


