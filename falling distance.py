def falling_distance(time):
    distance = 0.5*9.8*(time**2)
    return distance
for x in range(10):
    print(format(falling_distance(x),",.2f"))

        