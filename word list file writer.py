words=int(input("how many words do you wish to write to a file:"))
infile=open("word.txt","w")
for count in range(1,words+1):
    word=input("word"+ str(count)+":")
    infile.write(word+"\n")
infile.close()
print("words have been written to word.txt")
