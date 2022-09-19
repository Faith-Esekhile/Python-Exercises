name= input("enter the name of a file")
file=open(name,"r")
total=0
lines=file.readline()
print(lines)
while lines !="":
    for line in file:
        total=total+1
        if total <= 4:
            print(line)
line=file.readline()
file.close()
