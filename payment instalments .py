purchase = int(input("enter the amount of purchase ="))
installment=int(input("enter the number of payment installments"))
total_purchase=(0.05*purchase) + purchase
amount=total_purchase/installment
print("your total amount of purchase is =",total_purchase)
print("your installment cost is =",amount)