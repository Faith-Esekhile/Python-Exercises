'''def create_deck():
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
           '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,'Queen of Diamonds':10, 
            'King of Diamonds': 10}
    return deck 
def main():
    deck=create_deck()
    num_cards=int(input("how many cards should i deal"))  
    deal_cards(deck,num_cards)

def deal_cards(deck,number):
    hand_value=0
    if number > len(deck):
        number=len(deck)
    for count in range(number):
        card,value= deck.popitem()
        print(card)
        hand_value+=value
    print("value of this hand:",hand_value)
main()'''

'''LOOK_UP=1
ADD=2
CHANGE=3
DELETE=4
QUIT=5
def main():
    brithdays ={}
    choice=0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(brithdays)
        elif choice == ADD:
            add(brithdays)
        elif choice ==CHANGE:
            change(brithdays)
        elif choice == DELETE:
            delete(brithdays)
def get_menu_choice():
    print()
    print('friends and their birthdays')
    print("---------------------------") 
    print("1.look up a birthday")
    print("2.add up a birthday")
    print("3.change a birthday")
    print("4.delete a bithday")
    print("5.quit the program")
    print()
    choice = int(input("enter your choice:"))
    while choice < LOOK_UP or choice > QUIT:
        choice=int(input("enter a valid choice:"))
    return choice

def look_up(birthdays):
    name=input("enter a name:")
    print(birthdays.get(name,"not found"))

def add(birthdays):
    name=input("enter a name:")
    bday=input("enter a birthday:")
    if name not in birthdays:
        birthdays[name]=bday
    else:
        print("that entry already exists")


def change(birthdays):
    name=input("enter a name")
    if name in birthdays:
        bday=input("enter the new birthday:")
        birthdays[name]=bday
    else:
        print("the name is not found")

def delete(birthdays):
    name = input("enter a name")
    if name in birthdays:
        del birthdays[name]
    else:
        print("that name is not found")
main()'''

