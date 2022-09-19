#1
'''first_name=input("enter your first name")
second_name=input("enter your last name")
initials=first_name[0] + second_name[0]
print(initials.upper())
print(first_name +" "+ second_name.upper())
print(first_name[0] + second_name)'''

#2
''''string=input('enter a series of single digit numbers')
total=0
num_list=[]
for x in string:
    num_list.append(x)
for c in num_list:
    number=int(c)
    total=total+number
print(total)'''
  
#3
'''date=input("enter date in the following format mm/dd/yyyy")
str_date=date.split("/")
month_=int(str_date[0])
day=int(str_date[1])
if day >= 8 or month_ >= 32:
    print("invalid date")
else:
    month_=str(str_date[0])
    day=str(str_date[1])
    if str_date[0] == "01":
        month = "january"
    elif str_date[0] == "02":
        month = "february"
    elif str_date[0] == "03":
        month = "march"
    elif str_date[0] == "04":
        month = "april"
    elif str_date[0] == "05":
        month = "may"
    elif str_date[0] == "06":
        month = "june"
    elif str_date[0] == "07":
        month = "july"
    elif str_date[0] == "08":
        month = "august"
    elif str_date[0] == "09":
        month = "september"
    elif str_date[0] == "10":
        month = "october"
    elif str_date[0] == "11":
        month = "november"
    elif str_date[0] == "12":
        month = "december"
    print(month+" "+str_date[1]+","+str_date[2])'''

#4
'''string=input("enter a string to be converted to morse code :")
string.lower()
for x in string:
    if x == "a":
        print(".-",end=" ")
    if x == "b":
        print("-...",end=" ")
    if x == "c":
        print("-.-.",end=" ")
    if x == "d":
        print("-..",end=" ")
    if x == "e":
        print(".",end=" ")
    if x == "f":
        print("..-.",end=" ")
    if x == "g":
        print("--.",end=" ")
    if x == "h":
        print("....",end=" ")
    if x == "i":
        print("..",end=" ")
    if x == "j":
        print(".---",end=" ")
    if x == "k":
        print("-.-.",end=" ")
    if x == "l":
        print(".-..",end=" ")
    if x == "m":
        print("--",end=" ")
    if x == "n":
        print("-.",end=" ")
    if x == "o":
        print("---",end=" ")
    if x == "p":
        print(".--.",end=" ")
    if x == "q":
        print("--.-",end=" ")
    if x == "r":
        print(".-.",end=" ")
    if x == "s":
        print("...",end=" ")
    if x == "t":
        print("-",end=" ")
    if x == "u":
        print("..-",end=" ")
    if x == "v":
        print("...-",end=" ")
    if x == "w":
        print(".--",end=" ")
    if x == "x":
        print("-..-",end=" ")
    if x == "y":
        print("-.-",end=" ")
    if x == "z":
        print("--.",end=" ")
    if x == "0":
        print("-----",end=" ")    
    if x == "1":
        print(".----",end=" ")
    if x == "2":
        print("..---",end=" ")
    if x == "3":
        print("...--",end=" ")
    if x == "4":
        print("....-",end=" ")
    if x == "5":
        print(".....",end=" ")
    if x == "6":
        print("-....",end=" ")
    if x == "7":
        print("--...",end=" ")
    if x == "8":
        print("---..",end=" ")
    if x == "9":
        print("----.",end=" ")
    if x == " ":
        print("",end=" ")
    if x == ",":
        print("--.--",end=" ")
    if x == ".":
        print(".-.-.-",end =" ")
    if x == "?":
        print("..--..",end =" ")'''

#5
'''number=str(input("enter phone number in the format xxx-xxx-xxxx"))
number=number.split("-")
letter=""
letter2=""
for x in number[1]:
    if x == "a" or x == "b" or x== "c":
        x ="2"
        letter+=x
    elif x =="d"or x== "e" or x=="f":
        x ="3"
        letter+=x
    elif x =="g"or x== "h" or x=="i":
        x = "4"
        letter+=x
    elif x =="j"or x== "k" or x=="l":
        x="5"
        letter+=x
    elif x =="m"or x== "n" or x=="o":
        x="6"
        letter+=x
    elif x =="p"or x== "q" or x=="r" or x=="s":
        x="7"
        letter+=x
    elif x =="t"or x== "u" or x=="v":
        x="8"
        letter+=x
    elif x =="w"or x== "x" or x=="y" or x=="z":
        x="9"
        letter+=x
for x in number[2]:
    if x == "a" or x == "b" or x== "c":
        x ="2"
        letter2+=x
    elif x =="d"or x== "e" or x=="f":
        x ="3"
        letter2+=x
    elif x =="g"or x== "h" or x=="i":
        x = "4"
        letter2+=x
    elif x =="j"or x== "k" or x=="l":
        x="5"
        letter2+=x
    elif x =="m"or x== "n" or x=="o":
        x="6"
        letter2+=x
    elif x =="p"or x== "q" or x=="r" or x=="s":
        x="7"
        letter2+=x
    elif x =="t"or x== "u" or x=="v":
        x="8"
        letter2+=x
    elif x =="w"or x== "x" or x=="y" or x=="z":
        x="9"
        letter2+=x

print(number[0],letter,letter2,sep='-')'''

#6
#7

#8
def main(string):
    for x in string:
        if x == ".":
            position= string.find(".")
            index=position+1
            word=string[index]
            caps=word.upper()
            new=string.replace(x,caps)
            print(new)
string_=input("enter a string")
main(string_)



 