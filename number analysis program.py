numbers=[]
total=0
print("please enter 20 numbers")
for x in range (1,21):
    print("enter number",x ,end="")
    num=float(input(":"))
    total=total+num
    numbers.append(num)
average=total/20
print(min(numbers))
print(max(numbers))
print(total)
print(average)

