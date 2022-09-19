def is_prime(num):
    counter = 0
    for i in range(2,num):
        if num % i == 0:
            counter = counter + 1
    if counter == 0:
        return num
    

for i in range(2,100):
    print(is_prime(i))
