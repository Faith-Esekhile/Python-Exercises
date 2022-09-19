players=int(input("how many players are in your club:"))
infile=open("golf.txt","w")
for x in range(1,players+1):
    name=str(input("enter name:"))
    score=int(input("enter score:"))
    infile.write(name +"\n")
    infile.write(str(score) +"\n")
infile.close()
print("the scores and name have been written to golf.txt")

outfile=open("golf.txt","r")
name=outfile.readline()
while name != "":
    score=outfile.readline()
    name=name.rstrip("\n")
    print("name :"+name)
    print("score:"+score)
    name=outfile.readline()
outfile.close()