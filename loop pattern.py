'''for row in range(6):
    print("#",end="",sep="")
    for spaces in range(row):
        print(" ",end="",sep="")
    print("#",sep="" )'''

for r in range (7,0,-1):
    for c in range(r,0,-1):
        print("*",end="")
    print()
