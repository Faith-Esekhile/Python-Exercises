'''import vehicles

def main():
    used_car = vehicles.Car("audi",2007,21500,21500.0,4)
    print("make:",used_car.get_make())
    print("model:",used_car.get_model())
    print("mileage:",used_car.get_mileage())
    print("price:",used_car.get_price())
    print("number of doors:",used_car.get_doors())

main()'''

'''import vehicles

def main():
    car = vehicles.Car("bmw",2001,7000,15000.0,4)
    truck = vehicles.Truck("toyota",2002,40000,12000.0,"4wd")
    suv=vehicles.SUV("volvo",2000,3000,18500.0,5)

    print("used car inventory")
    print("------------------")

    print("the following car is in inventory")
    print("make:",car.get_make())
    print("model:",car.get_model())
    print("milleage:",car.get_mileage())
    print("price:",car.get_price())
    print("number of doors:",car.get_doors())
    print()

    print("the following pickup truck is in inventory")

    print("make:",truck.get_make())
    print("model:",truck.get_model())
    print("mileage",truck.get_mileage())
    print("price",truck.get_price())
    print("drive type:",truck.get_drive_type())
    print()


    print("the following SUV is in inventory")
    print("make:",suv.get_make())
    print("model:",suv.get_model())
    print("mileage:",suv.get_mileage())
    print("price:",suv.get_price())
    print("passanger capacity :",suv.get_pass_cap())
    print()

main()'''

'''import accounts

def main():
    print("enter the following data for a savings account")
    acct_num=input("Account number:")
    int_rate=float(input("interest rate:"))
    balance=float(input('balance'))

    savings = accounts.SavingsAccount(acct_num,int_rate,balance)
   
    print("enter the following data for a CD")
    acct_num=input("Account number")
    int_rate=float(input("interest rate:"))
    balance=float(input("balance:"))
    maturity=input("maturity date")

    cd=accounts.CD(acct_num,int_rate,balance,maturity)

    print("here is the data you enteted")
    print()
    print("savings Account")
    print("---------------")
    print("account number:" ,savings.get_account_num())
    print("interest rate:",savings.get_interest_rate())
    print("balance:$",format(savings.get_balance(),",.2f"),sep="")
    print()
    print("CD")
    print("------------")
    print("account number:",cd.get_account_num())
    print("interest rate:",cd.get_interest_rate())
    print("balance:$",format(cd.get_balance(),",.2f"),sep="")
    print("maturity date:",cd.get_maturity_date())
main()'''


import animals

def main():
    mammal=animals.Mammal("regular animal")
    dog=animals.Dog()
    cat=animals.Cat()

    print("here are some animals and the sound they make")
    print("----------------------------------------------")

    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)

def show_mammal_info(creature):
    if isinstance(creature,animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print("that is not a mammal")

main()



