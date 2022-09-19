test_list=["a","c","a","a","d","b","c","a","c","b","a","d","c","a","d","c","b","b","d","a"]
test=open("test.txt","r")
ans_list=[]
count=0
letter=0
for lines in test:
    lines=lines.rstrip("\n")
    ans_list.append(lines)
for index in test_list:
        if index == ans_list[letter]:
            letter=letter+1
            count=count+1
print("your score is",count,"/","20",)

    

