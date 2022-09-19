import random
number= random.randint(1,100)
print(number)
user=int(input("enter a number"))
count = 1
if user == number:
    print("congratulations you guessed the number right")
else:
    while user != number:
        if user > number:
             print("too high try again")
        elif user < number :
            print("too low try again")
        user=int(input("enter a number"))
        count = count + 1
    print("congratulations you guessed the number right ")
print("your number of guesses is ", count)