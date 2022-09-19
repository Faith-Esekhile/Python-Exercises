'''def main_w():
    outfile=open("philosophers.txt","w")
    outfile.write("john locke\n")
    outfile.write("david hume\n")
    outfile.write("edmund bruke\n")
    outfile.write("socrates\n")
    outfile.close()
main_w()'''

'''def main_r():
    infile = open("philosophers.txt","r")
    filecontent  = infile.read()
    infile.close()
    print(filecontent)
main_r()'''

'''def main_r():
    infile = open("philosophers.txt","r")
    line1=infile.readline()
    line2=infile.readline()
    line1=line1.rstrip("\n")
    line2=line2.rstrip("\n")
    infile.close()
    print(line1)
    print(line2)
main_r()'''

'''def main():
    print("enter three names of friends")
    name1=input("friend 1 :")
    name2=input("friend 2 :")
    name3=input("friend 3 :")

    myfile = open("friends.txt","w")
    myfile.write(name1 + "\n")
    myfile.write(name2 + "\n")
    myfile.write(name3 + "\n")

    myfile.close()

    print("the name were written to friends.txt")
main()

myfile = open("friends.txt","a")
myfile.write("eloho\n")
myfile.write("gwill\n")'''


'''def main():
    outfile=open("numbers.txt","w")
    num1=int(input("enter a number:"))
    num2=int(input("enter another number:"))
    num3=int(input("enter another number:"))

    outfile.write(str(num1)+"\n")
    outfile.write(str(num2)+"\n")
    outfile.write(str(num3)+"\n")

    outfile.close()
    print("data written to numbers.txt")
main()'''

'''def main():
    infile=open("numbers.txt","r")
    num1=int(infile.readline())
    num2=int(infile.readline())
    num3=int(infile.readline())
    infile.close()
    total = num1 + num2 +num3
    print("the numbers are:",num1,num2,num3)
    print("their total is",total)
main()'''

'''def main():
    num_days=int(input("for how many days do you have sales :"))
    sales_file=open("sales.txt","w")
    for count in range (1,num_days +1):
        sales=float(input("enter sales for day " + str(count) + ":" ))
        sales_file.write(str(sales)+"\n")
    sales_file.close()
    print("data has been written to sales.text")
main()'''

'''def main_r():
    sales_file=open("sales.txt","r")
    line  = sales_file.readline()
    while line !="":
        amount=float(line)
        print(format(amount,".2f"))
        line = sales_file.readline()
    sales_file.close()
main_r()'''

'''def main():
    num_videos=int(input("how many videos are in the project"))
    video_file=open("video_times.txt","w")
    print("enter the running times for each video")
    for count in range(1,num_videos+1):
        run_time=float(input( "video" + str(count) + ":"))
        video_file.write(str(run_time) +"\n")
    video_file.close()
    print("the times have been saved to video_times.txt")
main()'''

'''def main_r():
    video_file=open("video_times.txt","r")
    total=0
    count=0
    print("here are the running times for each video")
    for line in video_file:
        run_time=float(line)
        count += 1
        print("videos",count,":",run_time,sep='')
        total += run_time
    video_file.close()
    print("the total running time is ",total,"seconds")
main_r()'''

'''def main_w():
    num_emps=int(input("how many employee records do you want to create"))
    emp_file=open("employees.txt","w")
    for count in range (1,num_emps +1):
        print("enter data for employee",count,sep="")
        name=input("name:")
        id_num=input("id number:")
        dept=input("department:")
        emp_file.write(name + "\n")
        emp_file.write(id_num+"\n")
        emp_file.write(dept + "\n")
        print()
    emp_file.close()
    print("employee records written to employees.txt")
main_w()'''

'''def main():
    emp_file=open("employees.txt","r")
    name=emp_file.readline()
    while name != "":
        id_num=emp_file.readline()
        dept=emp_file.readline()
        name=name.rstrip("\n")
        id_num=id_num.rstrip("\n")
        dept= dept.rstrip("\n")
        print("name:",name)
        print("id:",id_num)
        print("dept:",dept)
        print()
        name=emp_file.readline()
    emp_file.close()
main()'''

'''def main():
    another = "y"
    coffee_file = open("coffee.txt","a")
    while another == "y" or another == "Y":
        print("enter the following coffee data")
        descr=input("description:")
        qty=int(input("quantity in pounds:"))
        coffee_file.write(descr + "\n")
        coffee_file.write(str(qty) + "\n")
        print("do you want to add another record?")
        another = input("y = yes ,anything else = no :")
    coffee_file.close()
    print("data appended to coffee.txt")
main()'''

'''def main():
    coffee_file=open("coffee.txt","r")
    descr=coffee_file.readline()
    while descr != "":
        qty=float(coffee_file.readline())
        descr = descr.rstrip("\n")
        print("description:",descr)
        print("quantity:",qty)
        descr=coffee_file.readline()
    coffee_file.close()
main()'''

'''def main():
    found = False
    search = input("enter a description to search for:")
    coffee_file = open("coffee.txt","r")
    descr=coffee_file.readline()
    while descr != "":
        qty=float(coffee_file.readline())
        descr=descr.rstrip("\n")
        if descr == search:
            print("description :",descr)
            print("quantity :",qty)
            print()
            found = True
        descr=coffee_file.readline()
    coffee_file.close()
    if not found:
        print("that item was not found in the file")
main()'''
import os
def main():
    found = False
    search = input("what coffee do you want to delete")
    coffee_file = open("coffee.txt","r")
    temp_file=open("temp.txt","w")
    descr=coffee_file.readline()
    while descr !="":
        qty =float(coffee_file.readline())
        descr=descr.rstrip("\n")
        if descr != search:
            temp_file.write(descr + "\n")
            temp_file.write(str(qty)+ "\n")
        else:
            found = True
        descr=coffee_file.readline()
    coffee_file.close()
    temp_file.close()
    
    os.remove('coffee.txt')
    os.rename("temp.txt","coffee.txt")

    if found:
        print("the file has been updated")
    else:
        print("that item was not found in the file")
main()

'''def main():
    num1=int(input('enter a number:'))
    num2=int(input('enter another number :'))
    result =num1/num2
    print(num1,'divided by',num2,'is',result)
main()'''

'''def main():
    num1=int(input("enter a number :"))
    num2=int(input("enter another number"))
    if num2 != 0:
        result=num1/num2
        print(num1,"divided by",num2, "is",result)
    else:
        print("cannot divide by zero")
main()'''

'''def main():
    hours=int(input("how many hours did you work"))
    pay_rate=float(input("enter hourly pay rate:"))
    gross_pay=hours*pay_rate
    print("gross pay : $",format(gross_pay, ",.2f"),sep="")
main()'''

'''def main():
    try:
        hours=int(input("how many hours did you work"))
        pay_rate=float(input("enter your hourly pay rate:"))
        gross_pay=hours*pay_rate
        print("gross pay $",format(gross_pay,",.2f"),sep="")
    except ValueError:
        print("ERROR: hours worked and hourly rate must be valid numbers")
main()'''

'''def main():
    filename=input("enter a filename:")
    infile =open(filename,'r')
    contents=infile.read()
    print(contents)
    infile.close()
main()'''

'''def main():
    filename=input("enter a filename:")
    try:
        infile =open(filename,"r")
        contents =infile.read()
        print(contents)
        infile.close()
    except IOError:
        print("an error occurred trying to read the file",filename)
main()'''

'''def main():
    total = 0.0
    try:
        infile = open('sales_data.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
        print(format(total, ',.2f'))
    except IOError:
            print('An error occurred trying to read the file.')
    except ValueError:
            print('Non-numeric data found in the file.')
    except:
        print('An error occurred.')
main()'''

'''def main():
    try:
        hours =int(input("how many hours did you work?"))
        pay_rate=float(input("enter you hourly pat rate:"))
        gross_pay=hours*pay_rate
        print('gross pay:',format(gross_pay,",.2f"),sep="")
    except ValueError as err:
            print(err)
main()'''

'''def main():
    total=0.0
    try:
        infile = open("sales_data.txt","r")
        for line in infile:
            amount=float(line)
            total+=amount
        infile.close()
        print(format(total,",.2f"))
    except Exception as err:
        print(err)
main()'''

'''def main():
    total = 0.0
    try:
        infile = open("sales_data.txt",'r')
        for line in infile:
            amount=float(line)
            total+=amount
        infile.close()
    except Exception as err:
        print(err)
    else:
        print(format(total, ",.2f"))
main()'''
             




















