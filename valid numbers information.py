numbers=[74,19,105,20,-2,67,77,124,-45,38]
valid_numbers=[]
for x in numbers:
    if x  >=1 and x<=100:
        valid_numbers.append(x)
print(valid_numbers)