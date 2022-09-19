'''def main():
    my_coin=Coin()
    print("this side is up:",my_coin.get_sideup())
    print("i am tossing the coin")
    my_coin.toss()
    print("this side is up:",my_coin.get_sideup())
main()'''


'''import coin
def main():
    my_coin=coin.Coin()
    print("this side is up:",my_coin.get_sideup())
    print("i am going to toss the coin ten times")
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())
main()'''

'''import bankaccount
def main():
    start_bal=float(input("enter your starting balance:"))
    savings=bankaccount.BankAccount(start_bal)
    pay=float(input("how much were you paid this week?"))
    print("i would deposit that into your account")
    savings.deposit(pay)
    print("your account balance iis $",format(savings.get_balance(),',.2f'),sep="")
    cash=float(input("how much would you like to withdraw?"))
    print("i will withdraw that from your account") 
    savings.withdraw(cash)
    print("your account balance is $",format(savings.get_balance(),',.2f'),sep='')
main()'''

'''import bankaccount2
def main():
    start_bal=float(input("enter your starting balance:"))
    savings=bankaccount2.BankAccount(start_bal)
    print(savings)
    pay=float(input("how many were you paid this week?"))
    print("i will deposit that into your account")
    savings.deposit(pay)
    print(savings)
    cash=float(input("how much would you like to withdraw"))
    print("i will withdraw that from your account")
    savings.withdraw(cash)
    print(savings)
main()'''

'''import coin
def main():
    coin1=coin.Coin()
    coin2=coin.Coin()
    coin3=coin.Coin()

    print("i have three coins with these sides up:")
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    print("i am tossing all three coins")
    print()
    coin1.toss() 
    coin2.toss()
    coin3.toss()

    print("now here are the sides that are up:")
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()
main()'''

'''import cellphone
def main():
    man=input("enter the manufacturer:")
    mod=input("enter the model number:")
    retail=float(input("enter the retail price:"))
    phone=cellphone.CellPhone(man,mod,retail)
    print("here is the data you entered")
    print("manufacturer:",phone.get_manufact())
    print("model number:",phone.get_model())
    print("retail price:$",format(phone.get_retail_price(),',.2f'),sep="")
main()'''

'''import cellphone
def main():
    phones=make_list()
    print("here is the data you entered")
    display_list(phones)
def make_list():
    phone_list=[]
    print("enter data for five phones")
    for count in range(1,6):
        print("phone number"+str(count)+":")
        man=input("enter the manufacturer")
        mod=input("enter the model number")
        retail=float(input("enter the retail price:"))
        print()
        phone=cellphone.CellPhone(man,mod,retail)
        phone_list.append(phone)
        print(phone_list)
    return phone_list
def display_list(phone_list):
    for items in phone_list:
        print(items.get_manufact())
        print(items.get_model())
        print(items.get_retail_price())
        print()
main()'''

'''import coin
def main():
    my_coin=coin.Coin()
    print(my_coin.get_sideup())
    flip(my_coin)
    print(my_coin.get_sideup())
def flip(coin_obj):
    coin_obj.toss()
main()'''

'''import pickle
import cellphone

FILENAME="cellphone.dat"
def main():
    again ="y"
    output_file=open(FILENAME,"wb")
    while again.lower()=="y":
        man=input("enter the manufacturer:")
        mod=input("enter the model number:")
        retail=float(input("enter the retail price:"))
        phone=cellphone.CellPhone(man,mod,retail)
        pickle.dump(phone,output_file)
        again=input("enter more phone data?(y/n):")
    output_file.close()
    print("the data was written to",FILENAME)
main()'''

'''import pickle
import cellphone
FILENAME="cellphone.dat" 
def main():
    end_of_file=False
    input_file=open(FILENAME,"rb")
    while not end_of_file:
        try:
            phone=pickle.load(input_file)
            display_data(phone)
        except EOFError:
            end_of_file=True
    input_file.close()
def display_data(phone):
    print("manufacturer:",phone.get_manufact())
    print("model number:",phone.get_model())
    print('retail price $',format(phone.get_retail_price(),',.2f'),sep="")
main()'''


import contact
import pickle

LOOK_UP=1
ADD=2
CHANGE=3
DELETE=4
QUIT=5

FILENAME="contacts.dat"
def main():
    mycontacts = load_contacts()
    choice=0
    while choice!=QUIT:
        
        choice=get_menu_choice()

        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
    save_contacts(mycontacts)
def load_contacts():
    try:
        input_file=open(FILENAME,"rb")
        contact_dct=pickle.load(input_file)
        input_file.close()
    except IOError:
        contact_dct={}
    return contact_dct
def get_menu_choice():
    print()
    print("menu")
    print("------------------------")
    print("1.look up a contact")
    print("2.add a new contact")
    print("3.change an existing contact")
    print("4.delete a contact")
    print("5.quit the program")
    print()
    choice = int(input("enter your choice:"))
    while choice<LOOK_UP  or choice > QUIT:
        choice=int(input("enter a valid choice:"))
    return choice
def look_up(mycontacts):
    name=input("enter a name:")
    print(mycontacts.get(name,"that is not found"))
def add(mycontacts):
    name=input("name:")
    phone=input("phone:")
    email=input("email:")
    entry=contact.Contact(name,phone,email)
    if name not in  mycontacts:
        mycontacts[name]=entry
        print("the entry has been added")
    else:
        print("that name already exists")
def change(mycontacts):
    name=input("enter a name:")
    if name in mycontacts:
        phone=input("enter the new phone number:")
        email=input("enter the new email address")
        entry=contact.Contact(name,phone,email)
        mycontacts[name]=entry
        print("information updated")
    else:
        print("that name is not found")
def delete(mycontacts):
    name=input("enter a name:")
    if name in mycontacts:
        del mycontacts[name]
        print("entry deleted")
    else:
        print("that name is not found")

def save_contacts(mycontacts):
    output_file=open(FILENAME,"wb")
    pickle.dump(mycontacts,output_file)
    output_file.close()
main()













