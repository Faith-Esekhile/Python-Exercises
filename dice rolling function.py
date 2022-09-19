import random
def roll(number_of_throws):
    throw_list=[]
    for x in range(number_of_throws):
        x=random.randint(1,6)
        throw_list.append(x)
    throw_list.sort()
    return throw_list
number=int(input("number of throws:"))
print(roll(number))
