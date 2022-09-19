 import random
MIN=1
MAX=10
for numbers in range(5):
    print("question",numbers+1)
    print(random.randint(MIN,MAX),'+',random.randint(MIN,MAX) ,"=")
