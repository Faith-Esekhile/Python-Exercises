infile=open("numbers.txt","r")
sum=0
count=0
for lines in infile:
    line=float(lines)
    count=count+1
    sum=sum+line
print(sum/count)