import math
people=int(input("enter the number of people attending the cook out:"))
hotdog_eat=int(input("enter the amount of hotdog each person will get"))
bun_pack=10
hotdog_pack=8
if people%bun_pack != 0:
    bun=(people//bun_pack)+1
else:
    bun=(people//bun_pack)
if  people%hotdog_pack !=0:
    hot=(people//hotdog_pack)+1
else:
    hot=(people//hotdog_pack)
bun_eat=bun*hotdog_eat
hot_eat=hot*hotdog_eat
print(" The minimum packages of bun required is ",bun_eat)
print(" The minimum packages of hotdog required is",hot_eat)
left_over_bun=(bun*bun_pack)-people
left_over_hotdog=(hot*hotdog_pack)-people
print("The left over bun would be",left_over_bun)
print("The leftover hotdog would be",left_over_hotdog)
