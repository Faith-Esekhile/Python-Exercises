import random
total=0
tot=0
for c in range(100):
    number=random.randint(0,100)
    print(number)
    if number%2 == 0:
        total=total+1
    elif number%2 != 0:
        tot=tot+1
print('there are', total ,'even numbers and', tot,' odd numbers')