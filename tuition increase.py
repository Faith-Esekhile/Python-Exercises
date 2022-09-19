pay=8000
year=5
print("year\t   fees")
for x in range(1,year+1):
        total= pay
        for c in range(x):
            increase=0.03*total
            total=total+increase
        print(x,"\t",(format(total,".1f")))


