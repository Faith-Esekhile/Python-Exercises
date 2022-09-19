loan=float(input("enter monthly cost for loan:"))
insurance=float(input("enter monthly cost for insurance:"))
gas=float(input("enter monthly cost for gas:"))
oil=float(input("enter monthly cost for oil:"))
tires=float(input("enter monthly cost for tires:"))
maintenance=float(input("enter monthly cost for maintenance:"))

def monthly_cost():
    total=loan+insurance+gas+oil+tires+maintenance
    print("the total monthly cost is ",total)
    return monthly_cost
def annual_cost():
    total=(loan+insurance+gas+oil+tires+maintenance)*12
    print("the total annual cost is ",total)
monthly_cost()
annual_cost()
