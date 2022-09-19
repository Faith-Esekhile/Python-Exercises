infile=open("faith.txt","r")
num=infile.readline()
while num != "":
    nums=infile.readline()
    print(num)
    print(nums)
    num=infile.readline()
infile.close()



