def is_prime():
    counter = 0
    for i in range(2,num):
        if num % i == 0:
            counter = counter + 1
            print(f"{num} can be divisible by {i}.")
    if counter > 0:
        print("it is not a prime number")
    else:
        print("it is a prime number")
num = int(input("Enter the number you want to check is prime: "))

if num < 2 and num >= 0:
    print(f"{num} is not prime number.")
elif num > 2:
   is_prime()
else:
    print(f"Please write number larger than 0.")


