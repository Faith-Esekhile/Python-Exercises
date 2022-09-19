shares_bought_sold=2000
amt_per_share_bought=40
stock_bought=shares_bought_sold*amt_per_share_bought
comm_bought=0.03*stock_bought
amt_per_share_sold=42.75
stock_sold=shares_bought_sold*amt_per_share_sold
comm_sold=0.03*stock_sold
profit_or_loss=(stock_sold-comm_sold)-(stock_bought-comm_bought)
print("The amount of money Joe paid for the stock is =",stock_bought)
print(" The amount of commission Joe paid his broker when he bought the stock is=",comm_bought)
print(" The amount for which Joe sold the stock is =",stock_sold)
print(" The amount of commission Joe paid his broker when he sold the stock si =",comm_sold)
print(" the amount of money that Joe had left when he sold the stock and paid his broker (both times) is ",profit_or_loss)
if profit_or_loss <1:
    print("he made a loss")
else:
    print(" he made profit")