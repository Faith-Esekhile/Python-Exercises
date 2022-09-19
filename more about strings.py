'''name = "juliet"
for ch in name:
    print(ch)
print(name)'''

'''def main():
    count=0
    my_=input("enter a sentence:")
    for ch in my_:
        if ch == "T" or ch == 't':
            count += 1
    print('the letter t appers',count,"times")
main()'''

'''my_ = "roses are red"
ch = my_[6]
print(ch)
my_ = "roses are red"
print(my_[0],my_[6],my_[10])'''

'''my_ = "roses are red"
print(my_[-1],my_[-2],my_[-13])'''

'''city="boston"
index =0
while index < 7:
    print(city[index])
    index += 1'''
'''city="boston"
size =len(city)
city ="boston"
index=0
while index < len(city):
    print(city[index])
    index += 1'''

'''message = "hello" + "world"
print(message)'''
'''first_name='emily'
last_name="yeager"
full_name=first_name + " " + last_name
print(full_name)

letters ="abc"
letters += 'def'
print(letters)'''

'''def main():
    name = "carmen"
    print("the name is brown")
    name=name+"brown"
    print("now the name is",name)
main()'''

'''full_name = "patty lynn smith"
middle_name= full_name[6:10]
print(middle_name)'''

'''full_name="patty lynn smith"
first_name=full_name[:5]
print(first_name)'''

'''full_name='patty lynn smith'
last_name=full_name[11:]
print(last_name)'''

'''full_name="patty lynn smith"
my_=full_name[:]
print(my_)'''

'''letters = "abcdefghijklmnopqrstuvwxyz"
my_=letters[0:len(letters):2]
print(my_)'''

'''full_name="patty lynn smith"
last_name=full_name[-3:]
print(last_name)'''


'''import login

def main():
    first =input("enter your first name:")
    last=input("enter your last name")
    idnumber=input("enter your student id:")

    print("your system login name is")
    print(login.get_login_name(first,last,idnumber))
main()'''

'''def main():
    user_=input('enter a ')
    print('this is what i found about the ')
    if user_.isalnum():
        print("the  is alphanumeric")
    if user_.isdigit():
        print("the  contains on digits")
    if user_.isalpha():
        print("the  is alphabetic")
    if user_.isspace():
        print('the  contains white space characters')
    if user_.islower():
        print("the letters in the  are all lower case")
    if user_.isupper():
        print("the letter in the  are all uppercase")
main()'''

'''def main():
    user_ = input('Enter a : ')
    print('This is what I found about that :')
    if user_.isalnum():
        print('The  is alphanumeric.')
    if user_.isdigit():
        print('The  contains only digits.')
    if user_.isalpha():
        print('The  contains only alphabetic characters.')
    if user_.isspace():
        print('The  contains only whitespace characters.')
    if user_.islower():
        print('The letters in the  are all lowercase.')
    if user_.isupper():
        print('The letters in the  are all uppercase.')
main() '''  

'''letters = 'WXYZ'
print(letters,letters.lower())'''

'''letters ='abcd'
print(letters,letters.upper())'''

'''again = "y"
while again.lower()=="y":
    print("hello")
    print("do you want to see that again?")
    again= input("y=yes,anything else=no")'''

'''filename=input("enter the filename:")
if filename.endswith(".txt"):
    print("that is the name of the text file")
elif filename.endswith(".py"):
    print("that is the name of a python source file.")
elif filename.endswith(".doc"):
    print("that is the name of the word processing document")
else:
    print("unknown file type")'''

''' = 'four score and seven years ago'
position=.find("seven") 
if position != -1:
    print('the word "seven" was found at index',position)
else:
    print('the word "seven" was not found')'''

'''="four score and seven years ago"
new_=.replace("years","days")
print(new_)'''

'''import login

def main():
    password=input("enter your password")
    while not login.valid_password(password):
        print("that password is not valid")
        password=input("enter your password:")
    print("that is a valid password")
main()'''

'''def main():
    for count in range(1,10):
        print("z"*count)
    for count in range(8,0,-1):
        print("z"*count)
main()'''

'''def main():
    my_="one two three four"
    word_list=my_.split()
    print(word_list)
main()'''

'''def main():
    date_string = "11/26/2018"
    date_list=date_string.split("/")
    print("month",date_list[0])
    print("day:",date_list[1])
    print("year:",date_list[2])
main()'''






















