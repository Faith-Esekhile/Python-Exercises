'''keepgoing = "yes"
while keepgoing == "yes":
    name=input("what is your name :")
    keepgoing= input("do you want to enter another name if so enter yes if not enter no:")'''
'''max_temp=102.5
temp=float(input("enter temperature of substance in celsius:"))
while temp > max_temp:
    print("the temperature is too high")
    print("turn down the thermostart and wait")
    print("5 minutes,take down the temperature")
    print("enter it again")
    temp=float(input("enter temperature of substance in celsius:"))
print("the temperature is acceptable")
print("check it again in 15 min")'''
'''keep_going = 'y' 
while keep_going == 'y': 
    sales = float(input('Enter the amount of sales: ')) 
    comm_rate = float(input('Enter the commission rate: ')) 
    commission = sales * comm_rate      
    print('The commission is $',format(commission, ',.2f'), sep='')'''
'''print("i will display the numbers 1 through 5")
for num in [1,2,3,4,5]:  
    print(num) '''
'''print("i will display the odd numbers 1 through 9")
for num in [1,3,5,7,9]:
    print(num)'''
'''for name in ["winken","blinken","nod"]:
    print(name)'''
'''for num in range (5):
    print(num)'''
'''for num in  [0,1,2,3,4]:
    print(num)'''
'''for x in range (5):
    print("hello world")'''
'''for num in range (1,10,2):
    print(num)'''
'''print("number\tsquare")
   for number in range (1,11):
square = number**2
   print(number,"\t",square)
print("number\tsquare")
for numbers in  range (1,6):
    square=numbers**2
    print(numbers,'\t',square)'''
'''start=int(input("enter starting number"))
end=int(input("enter the ending number"))
for numbers in range (start,end+1):
    square=numbers**2
    print(numbers,"\t",square)'''
'''for num in range (10,0,-2):
    print(num)'''
'''for number in range (6):
    print(number)'''
'''MAX=5
total=0
print("the program calculates the sum of ",MAX,"numbers")
for counter in  range (MAX):
    number=int(input("enter a number:"))
    total=total+number
print("the total is", total)'''
'''tax_factor=0.0065
print("enter the property lot number or zero to end")
lot=int(input("enter lot number"))
while lot != 0:
    value=int(input("enter the property value"))
    tax=value*tax_factor
    print("property tax :$",format(tax,",.2f"),sep="")
    print("enter the next lot number or zero to end")
    lot=int(input("lot number:"))'''
'''mark_up = 2.5
another="y"
while another == "y" or another =="y":
    wholesale=float(input("enter the items wholesale cost"))
    retail=wholesale*mark_up
    print("retail price:",format(retail ,",.2f"),sep="")
    another=input("do you have another item enter y for yes")'''
'''mark_up=2.5
another ="y"
while another  == "Y" or another == "y":
    wholesale=float(input("enter the items whole cost:"))
    while wholesale < 0:
        print("error:the cost cannot be negative ")
        wholesale=float(input("enter the correct wholesale cost:"))
    retail = wholesale*mark_up
    print("retail price $",format(retail,",.2f"),sep="" )
    another=input("do you have another item? enter y for yes:")'''
'''num_students=int(input("how many  student do you have?:"))
num_test_scores=int(input("how many test scores per student?:"))
for student in range(num_students):
    total=0
    print("student number",student +1)
    for test_num in range(num_test_scores):
        print("test number",test_num+1,end="")
        score=float(input(":"))
        total=total+score
    average =total/num_test_scores
    print("the average for student number",student+1,"is",average)'''
'''row=int(input("how many rows?"))
cols=int(input("how many columns"))
for r in range (row):
    for c in range(cols):
        print("*",end="")
    print()'''
'''base_size =8
for r in range (base_size):
    for c in range(r+3):
        print("*",end="")
    print()'''
'''num_steps=6
for r in range(num_steps):
    for c in range(r):
        print(" ",end="")
    print("#")'''

    



















    














