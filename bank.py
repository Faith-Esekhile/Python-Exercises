import bankaccount2
def main():
    start_bal=float(input("enter your strting balance:"))
    savings=bankaccount2.BankAccount(start_bal)
    pay=float(input("how much were you pain this week"))
    print("i will deposit into your account")
    savings.deposit(pay)

    print("your account balance is $",format(savings.get_balance(),",.2f"),
    sep='')

    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)
    print('Your account balance is $', format(savings.get_balance(), ',.2f'),sep='')
main()