infile=open('numbers.txt','r')
sum=0
for lines in infile:
    num=float(lines)
    sum=sum+num
print(sum)
infile.close()