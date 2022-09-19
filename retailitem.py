class RetailItem:
    def __init__(self,desc,invt,price):
        self.__desc=desc
        self.__invt=invt
        self.__price=price

    def set_desc(self,desc):
        self.__desc=desc
    def set_invt(self,invt):
        self.__invt=invt
    def set_price(self,price):
        self.__price=price

    def get_desc(self):
        return self.__desc
    def get_invt(self):
        return self.__invt
    def get_price(self):
        return self.__price
    
    def __str__(self):
        return "description :"+self.__desc + "\n" \
                "units:"+ str(self.__invt) + "\n" \
                "price:"+ str(self.__price)
        
        
item1=RetailItem("jacket",12,59.95)
item2=RetailItem("designer jenes",40,34.95)
item3=RetailItem("shirt",20,24.95)
 
print(item1,end="\n\n")
print(item2,end="\n\n")
print(item3)