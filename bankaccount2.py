class BankAccount:
    def __init__(self,bal):
        self.balance=bal
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("error:innsufficient funds")
    def get_balance(self):
        return self.balance
    def  __str__(self):
        return "the balance is $" + format(self.balance,',.2f')