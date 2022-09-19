'''num_days=5
def main():

    sales=[0]*num_days
    index=0
    print("enter the sales for each day")
    while index < num_days:
        print('day #',index + 1,";",sep="",end="")
        sales[index]=float(input())
        index+=1
    print("here are the values you entered")
    for value in sales:
        print(value)
main()'''

'''list1=[1,2,3,4]
list2=[5,6,7,8]
list3=list1+list2
print(list3)'''

'''days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
middays=days[2:5]
print(middays)'''

'''def main():
    prod_nums=["v475","f987","q143","r688"]
    search=input("enter a product number:")
    if search in prod_nums:
        print(search,"was found in the list")
    else:
        print(search,"was not found in the list")
main()'''

'''mylist=[1,2,3,4]
index=0
while index < 4:
    print(mylist[index])
    index+=1'''

'''def main():
    name_list=[]
    again ="y"
    while again =="y":
        name=input("enter a name")
        name_list.append(name)
        print("do you want to add another name")
        again=input("y = yes and anything else = no")
        print()
    print("here are the names you entered")
    for name in name_list:
        print(name)
main()'''



'''def main():
    food=["pizza","burger","chips"]
    print('here are the items in the food list')
    print(food)
    
    item =input('which item should i change')
    try:
        item_index=food.index(item)
        new_item=input("enter the new value:")
        food[item_index]=new_item
        print("here is the revised list:")
        print(food)
    except ValueError:
        print("that item was not found in the list")
main()'''

'''def main():
    names=["james","kathryn","bill"]
    print("the list before the insert:")
    print(names)
    names.insert(0,"joe")
    print('the list after the insert')
    print(names)
main()'''

'''my_list=[9,1,0,2,8,6,7,4,5,3]
print("original order:",my_list)
my_list.sort()
print("sorted order:",my_list)'''

'''def main():
    food = ['pizza','burgers','chips']
    print('here are the items in the food list')
    print(food)

    item = input("which item should i remove?")
    try:
        food.remove(item)
        print("here is the reversed list")
        print(food)
    except ValueError:
        print('item was not found in the list')
main()'''

'''my_list=[1,2,3,4,5]
print("original order:",my_list)
my_list.reverse()
print("reversed:",my_list)'''

'''my_list=[1,2,3,4,5]
print("before deletion:",my_list)
del my_list[2]
print('after deletion:',my_list)'''

'''my_list=[5,4,3,2,50,40,30]
print("the lowest value is",min(my_list))
print("the highest value is",max(my_list))'''

'''list1=[1,2,3,4]
list2=[]
for item in list1:
    list2.append(item)
print(list2)'''

'''num_employees=6
def main():
    hours=[0]*num_employees
    for index in range (num_employees):
        print('enter the hours worked by employee',
        index+1,":",sep="",end="")
        hours[index]=float(input())
    pay_rate=float(input("enter the hourly pay rate"))
    for index in range(num_employees):
        gross_pay=hours[index]*pay_rate
        print('gross pay for employee',index+1,":$",
        format(gross_pay,",.2f"),sep="")
main()'''
'''ef main():
    numbers=[2,4,8,10]
    total=0
    for value in numbers:
        total+=value
    print('the total of the elements is',total)
main()'''

'''def main():
    scores=[2.5,7.3,6.5,4.0,5.2]
    total=0.0
    for value in scores:
        total+= value
    average = total/len(scores)
    print("the average of the elements is",average)
main()'''

'''def main():
    numbers=[2,4,6,8,10]
    print('the total is',get_total(numbers))
def get_total(value_list):
    total=0
    for num in value_list:
        total+=num
    return total
main()'''

'''def main():
    numbers=get_values()
    print("the numbers in the new list are")
    print(numbers)
def get_values():
    values=[]
    again='y'
    while again =='y':
        num=int(input("enter a number"))
        values.append(num)
        print("do you want to enter another number")
        again=input("y=yes,anything else = no")
        print()
    return values
main()'''

'''def main():
    scores=get_scores()
    total=get_total(scores)
    lowest=min(scores)
    total-=lowest
    average=total/(len(scores)-1)
    print('the average with the lowest score dropped is',average)


def get_scores():
    test_scores=[]
    again="y"
    while again == "y":
        value=float(input("enter a test score"))
        test_scores.append(value)
        print('do you want to add another score')
        again=input("y=yes,anything else = no:")
        print()
    return test_scores
def get_total(value_list):
    total=0.0
    for num in value_list:
        total+=num
    return total
main()'''

'''def main():
    cities=['new york','boston','atlanta','dallas']
    outfile=open('cities.txt','w')
    outfile.writelines(cities)
    outfile.close()
main()'''

'''def main():
    cities=["new york","boston","atlanta","dallas"]
    outfile=open('cities.txt','w')
    for item in cities:
        outfile.write(item + '\n')
    outfile.close()
main()'''

'''def main():
    infile=open("cities.txt","r")
    cities=infile.readlines()
    infile.close()
    index=0
    while index <len(cities):
        cities[index]=cities[index].rstrip('\n')
        index+=1
    print(cities)
main()'''

'''def main():
    infile=open("numberslist.txt","r")
    numbers=infile.readline()
    infile.close()
    index=0
    while index<len(numbers):
        numbers[index]=int(numbers[index])
        index+=1
    print(numbers)
main()'''

'''numbers=[0]*5
index=0
while index < len(numbers):
    numbers[index]=99
    index+=1
print(numbers)'''

'''import random
rows=3
cols=4

def main():
    values=[[0]*5,[0]*5,[0]*5,]

    for r in range(rows):
        for c in range(cols):
            values[r][c]=random.randint(1,100)
    print(values)
main()'''

'''my_le=(1,2,3,4,5)
print(my_le)'''

'''names=('holly','warren','ashley')
for n in names:
    print(n)'''

'''names=("holly","warren","ashley")
for i in range(len(names)):
    print(names[i])'''

'''number_le=(1,2,3)
number_list=list(number_le)
print(number_list)'''

'''srt_list=['one','two','three']
str_le=le(srt_list)
print(str_le)'''

import matplotlib.pyplot as plt

def main():
    x_coords=[0,1,2,3,4]
    y_coords=[0,3,1,5,2]

    plt.plot(x_coords,y_coords)
    plt.show()
main()


'''matplotlib.pyplot import
def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    plt.plot(x_coords, y_coords)
    plt.show()
main()'''   








