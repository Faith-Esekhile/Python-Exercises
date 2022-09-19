file=input("enter the name of the file")
count=0
infile=open(file,"r")
for lines in infile:
    line_s=str(lines)
    count+=1
    print("line",count,".",line_s)
infile.close()
    
