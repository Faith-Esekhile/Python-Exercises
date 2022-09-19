'''ju_moon_rad={"lo":"1821.6","europa":"1560.8","ganymede":"2634.1","callisto":"2410.3"}
ju_moon_g={"lo":"1.794","europa":"1.314","ganymede":"1.428","callisto":"1.235"}
ju_moon_T={"lo":"1.769","europa":"3.551","ganymede":"7.154","callisto":"16.689"}
Moon=input("enter a galilean moon of jupiter:")
moon=Moon.lower()
for key  in ju_moon_g:
    if key == moon:
        print("radius:",ju_moon_g[key])
for key  in ju_moon_g:
    if key == moon:
        print("surface gravity:",ju_moon_g[key])
for key  in ju_moon_T:
    if key == moon:
        print("orbital period:",ju_moon_T[key])'''


'''import random
count=0
num=0
USA={"alabama": "montgomery" , "Alaska":"Juneau","Arizona":"Phoenix ", "Arkansas":"Little Rock","California":"Sacramento", "olorado ":"Denver",
"Connecticut":" Hartford","Delaware ":"Dover","Florida ":"Tallahassee" ,"georgia" :"Atlanta" , "Hawaii":"Honolulu","Idaho":"Boise" ,
"Illinois": "Springfield","Indiana":"Indianapolis" ,"Iowa":"Des Moines" , "Kansas":"Topeka" ,"Kentucky":"Frankfort ","Louisiana":"Baton Rouge" ,
"Maine":"Augusta" , "Maryland":"Annapolis ", "Massachusetts":"Boston","Michigan":"Lansing ", "Minnesota":"St. Paul","Mississippi":"Jackson" ,
"Missouri":"Jefferson City" ,"Montana":"Helena" ,"Nebraska":"Lincoln","Nevada":"Carson City","New Hampshire":"Concord" ,"New Jersey":"Trenton" ,
"New Mexico":"Santa Fe" ,"New York ":"Albany" ,"North Carolina":"Raleigh","North Dakota":"Bismarck" ,"Ohio": "Columbus",
"Oklahoma":"Oklahoma City","Oregon":"Salem ","pennsylvania":"Harrisburg" ,"Rhode Island":"Providence","South Carolina":"Columbia" ,
"South Dakota":"Pierre ","Tennessee":"Nashville" ,"Texas":"Austin","Utah":"Salt Lake City","Vermont": "Montpelier" ,
"Virginia":"Richmond","Washington":"Olympia" ,"West Virginia":" Charleston","Wisconsin": "Madison","Wyoming":"Cheyenne"}
for key in USA:
    state = key
    print("what is the capital of ",key,":")
    answer=input("answer:")
    answer=answer.lower()
    if answer == USA[key]:
        count=count+1
    else:
        num=num+1
print("your score is",count,"and you failed",num)'''


'''####
codes={"A":"%","a":"9","B":"@","b":"#","C":"$","c":"1"," ":" "}
infile=open('file.txt','r')
content=infile.readline()
while content != " ":
    for line in content:
      for key in codes:
          if line == key:
              line = codes[key]
              outfile=open("file2.txt","w")
              outfile.write(line)
    content=infile.readline()
outfile.close()   
infile.close()'''

'''###
myset=set()
infile =open("coffee.txt","r")
content=infile.readline()
while content != " ":
    myset.add(content)
    content=infile.readline()
infile.close()
print(myset)###'''

import random


