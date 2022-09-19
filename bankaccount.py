class BankAccount:
    def __init__(self,bal):
        self.balance=bal
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("error: insufficient funds")
    def get_balance(self):
        return self.balance