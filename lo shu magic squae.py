import random
rows=3
cols=3
def magic(di_list):
    di_list=[[0]*3,[0]*3,[0]*3]
    for r in range(rows):
        for c in range(cols):
            num=int(input("enter a number:"))
            di_list[r][c]=num
    print(di_list)
    totalcol1=di_list[0][0] + di_list[1][0]+di_list[2][0]
    totalcol2=di_list[0][0] + di_list[1][1]+di_list[2][1]
    totalcol3=di_list[0][2] + di_list[1][2]+di_list[2][2]
    totalrol1=di_list[0][0] + di_list[0][1]+di_list[0][2]
    totalrol2=di_list[1][0] + di_list[1][1]+di_list[1][2]
    totalrol3=di_list[2][0] + di_list[2][1]+di_list[2][2]
    totaldia1=di_list[0][0] + di_list[1][1]+di_list[2][2]
    totaldia2=di_list[2][0] + di_list[1][1]+di_list[0][2]
    
    if totalcol1 and totalcol2 and totalcol3 and totalrol1 and totalrol2 and totalrol3 and totaldia1 and totaldia2 == 15:
        print("it is a lo shu magic square")
    else:
        print("it is not a lo shu magic square")

my_list=[[0]*3,[0]*3,[0]*3]
magic(my_list)