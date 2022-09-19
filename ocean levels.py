mili = 1.6
year = 25
print("year\t   ocean level")
for x in range (1,year+1):
    total=0
    for c in range (x):
        total=total+mili
    print( x,'\t',(format(total,".1f")))

