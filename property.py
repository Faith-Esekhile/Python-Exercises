property_value=float(input('enter your property value:'))
access_value=property_value*0.6
tax=access_value/100
property_tax=tax*0.72
print(access_value)
print( format,(property_tax,".2f"))