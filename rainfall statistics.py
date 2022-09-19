rainfall_list=[]
total=0
for x in range(1,13):
    print("enter the total amount of rain fall in month", x)
    rain=float(input('rainfall:'))
    total=total+rain
    rainfall_list.append(rain)
average=total/12
high=max(rainfall_list)
low=min(rainfall_list)
print(total)
print(average)
print(high)
print(low)

