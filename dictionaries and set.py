'''phonebook={"chris":"555-111","katie":"555-222","joanne":"555-3333"}
#print(phonebook["chris"])
#print(phonebook["joanne"])
phonebook["joe"]="555-0123"
phonebook["chris"]="555-4444"
#print(phonebook)
del phonebook["chris"]
num_item=len(phonebook)
print(phonebook)
print(num_item)'''

'''test_scores={"kayla":[88,83,100],
             "luis":[95,74,81],
             "sophie":[72,88,91],
             "ethan":[70,75,78]}
print(test_scores)
print(test_scores["sophie"])
kayla_scores=test_scores["kayla"]
print(kayla_scores)'''

'''mixed_up={'abc':1,999:"yada yada",
         (3,6,9):[3,6,9]}
print(mixed_up)'''

'''employee={'name':"kelvin smith",
           "id":12345,"payrate":25.75}
print(employee)'''

'''phonebook={}
phonebook['chris']="555-1111"
phonebook["katie"]="555-2222"
print(phonebook)'''

phonebook={"chris":"555-111",
            "katie":"555-2222",
             "joanne":"555-3333"}
for key in phonebook:
    print(key)
   # print(key,phonebook[key])

'''phonebook={"chris":"555-111",
            "katie":"555-222",}
#print(phonebook)
phonebook.clear()
print(phonebook)'''

'''phonebook={"chris":"555-111","katie":"555-222"}
value=phonebook.get("katie","entry not found")
print(value)'''

'''phonebook={"chris":"555-111","katie":"555-222",
            "joanne":"555-222"}
print(phonebook.items())'''

'''phonebook = {'Chris':'555−1111','Katie':'555−2222', 
              'Joanne':'555−3333'} 
for key,value in phonebook.items(): 
    print(key, value)'''

'''phonebook={'chris':'555−1111','Katie':'555−2222', 
              'Joanne':'555−3333'}
phone_num=phonebook.pop("chris",'enter not found')
print(phone_num)'''

'''phonebook={"chris":"555-111","katie":"555-222","joanne":"333-555"}
for val in phonebook.values():
    print(val)'''

###################SETS

'''myset=set()

myset=set(['a','b','c'])

myset=set('abc')

myset=set=("aaabc")



print(myset)'''

'''myset=set([1,2,3,4,5])
print(len(myset))'''
    
'''myset=set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)'''

'''set1=set([1,2,3])
set2=set([8,9,10])
set1.update(set2)
print(set1)'''

'''myset=set([1,2,3])
myset.update("abc")
print(myset)'''

'''myset=set([1,2,3,4,5])
print(myset)
myset.remove(1)
print(myset)
myset.discard(5)
print(myset)'''

'''myset=set([1,2,3,4,5])
print(myset)
myset.clear()
print(myset)'''

'''myset=set(["a","b","c"])
for val in myset:
    print(val)'''

'''myset = set([1,2,3])
if 99 not in myset:
    print("the value 99 is not in the set")'''

'''set1=set([1,2,3,4])
set2=set([3,4,5,6])
set3=set1.union(set2)
print(set3)'''

'''set1=set([1,2,3,4])
set2=set([3,4,5,6])
set3=set1|set2
print(set3)'''

'''set1=set([1,2,3,4])
set2=set([3,4,5,6])
set3=set1.intersection(set2)
print(set3)'''

'''set1=set([1,2,3,4])
set2=set([3,4,5,6])
set3=set1&set2
print(set3)'''

'''set1=set([1,2,3,4])
set2=set([3,4,5,6])
set3=set1.difference(set2)
print(set3)'''

'''set1=set([1,2,3,4])
set2=set([3,4,5,6])
set3=set1-set2
print(set3)'''

'''set1=set([1,2,3,4])
set2=set([3,4,5,6])
set3=set1.symmetric_difference(set2)
print(set3)'''

'''set1=set([1,2,3,4])
set2=set([3,4,5,6])
set3=set1^set2
print(set3)'''

'''set1=set([1,2,3,4])
set2=set([2,3])
set2.issubset(set1)
set1.issuperset(set2)'''

'''set1=set([1,2,3,4])
set2=set([2,3])
set2<=set1
set1>=set2
set1<=set2'''

'''baseball=set(["jodi","carmen","aida","alicia"])
basketball=set(["eva","carmen","alicia","sarah"])
print("the following student are on the baseball team:")
for name in baseball:
    print(name)
print()
print("the following students are on the basketball team")
for name in basketball:
    print(name)
print()
print("the following students play both baseball and basketball:")
for name in baseball.intersection(basketball):
    print(name)
print()
print("the following students play either baseball or basketball ")
for name in baseball.union(basketball):
    print(name)
print()
print("the following students play baseball but not basketball:")
for name in baseball.difference(basketball):
    print(name)
print()
print("the following students play one sport,but not both:")
for name in baseball.symmetric_difference(basketball):
    print(name)'''

'''import pickle
phonebook={"chris":"555-111",
            "katie":"555-2222",
            "joanne":"555-3333"}
output_file=open("phonebook.dat","wb")
pickle.dump(phonebook,output_file)
output_file.close()'''

'''import pickle
def main():
    again="y"
    output_file=open("info.dat","wb")
    while again.lower()=="y":
        save_data(output_file)
        again=input("enter more data (y/n:")
    output_file.close()
def save_data(file):
    person={}
    person["name"]=input("name")
    person["age"]=int(input("age:"))
    person["weight"]=float(input("weight:"))
    pickle.dump(person,file)
main()'''

'''import pickle
def main():
    end_of_file=False
    input_file=open("info.dat","rb")
    while not end_of_file:
        try:
            person=pickle.load(input_file)
            display_data(person)
        except EOFError:
            end_of_file=True
    input_file.close()
def display_data(person):
    print("name",person["name"])
    print("age",person["age"])
    print("weight:",person["weight"])
    print()
main()'''








