def game():
    import random
    comp=random.randint(1,3)
    user=str(input("enter rock or paper or scissors :"))
    if user == "rock" or user == "paper" or user =="scissors":
        if user == "rock":
            user = 1
        elif user == "paper":
           user = 2
        elif user == "scissors":
           user = 3
        if comp == 1:
            print(" computer entered rock")
        elif comp == 2:
            print("computer entered paper")
        elif comp == 3:
            print("computer entered scissors")
        if comp == 1 and user == 3:
            print("you loose")
        elif comp == 3 and user == 2:
            print("you loose")
        elif comp == 2 and user == 1:
            print("you loose")
        else:
            if user == comp:
                    print("it is tie enter again to determine winner")
                    game()
            else:
                print("you win")
    else:
        print("invalid entry")
game()

   

    