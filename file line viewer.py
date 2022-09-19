try:
    file=input("enter the name of the file :")
    listt=[]
    count=0
    infile=open(file,"r")
    for lines in infile:
        count=count+1
        lines=lines.rstrip("\n")
        new_list=listt.append(lines)
    print(count)
    infile.close()
    view=int(input("enter the number of lines you want to view"))
    infile=open(file,"r")
    for x in range(1,view+1):
        file_line=infile.readline()
        print(file_line)
    infile.close()
except IOError:
    print("The file cannot be found")
except ValueError:
    print("file consists of numbers")
except IndexError:
    print("line number is outside range of data")
except:
    print("an error occured")
    
