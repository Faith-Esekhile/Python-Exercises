class Patient:
    def __init__(self,fname,mname,lname,address,city,state,ZIP,phone,ename,ephone):
        self.__fname=fname
        self.__mname=mname
        self.__lname=lname
        self.__address=address
        self.__city=city
        self.__state=state
        self.__ZIP=ZIP
        self.__phone=phone
        self.__ename=ename
        self.__ephone=ephone

    def set_fname(self,fname):
        self.__fname=fname
    def set_mname(self,mname):
        self.__mname=mname
    def set_lname(self,lname):
        self.__lname=lname
    def set_address(self,address):
        self.__address=address
    def set_city(self,city):
        self.__city=city
    def set_state(self,state):
        self.__state=state
    def set_ZIP(self,ZIP):
        self.__ZIP=ZIP
    def set_phone(self,phone):
        self.__phone=phone
    def set_ename(self,ename):
        self.__ename=ename
    def set_ephone(self,ephone):
        self.__ephone=ephone

    def get_fname(self,):
        return self.__fname
    def get_mname(self):
        return self .__mname
    def set_lname(self):
        return self.__lname
    def set_address(self,address):
        return self.__address
    def set_city(self):
        return self.__city
    def set_state(self):
        return self.__state
    def set_ZIP(self):
        return self.__ZIP
    def set_phone(self):
        return self.__phone
    def set_ename(self):
        return self.__ename
    def set_ephone(self):
        return self.__ephone
 

class Procedure:
    def __init__(self,pname,date,practitioner,charge):
        self.__pname=pname
        self.__date=date
        self.__practitioner=practitioner
        self.__charge=charge

    def set_pname(self,pname):
        self.__pname=pname
    def set_date(self,date):
        self.__date=date
    def set_practitioner(self,practitioner):
        self.__practitioner=practitioner
    def set_charge(self,charge):
        self.__charge=charge
    
    def get_pname(self):
        return self.__pname
    def get_date(self):
        return self.__date
    def get_practitioner(self):
        return self.__practitioner
    def get_change(self):
        return self.__change


    def __str__(self):
        return
        return super().__str__()