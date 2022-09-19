def mon_amt(num,amt,rate,):
    pay=(rate*amt)/(1-((1+rate))**(-num))
    return pay
loan_amt =float(input("enter loan amount :"))
mon_int=float(input("enter monthly intrest rate as percentage"))
month=int(input("enter desired amount of months"))
pay=mon_amt(month,loan_amt,mon_int)
print(pay)

