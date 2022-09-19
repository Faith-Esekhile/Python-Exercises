class Employee:
    def __init__(self,name,idno,dept,job):
        self.__name=name
        self.__idno=idno
        self.__dept=dept
        self.__job=job
    
    def set_name(self,name):
        self.__name=name
    def set_idno(self,idno):
        self.__idno=idno
    def set_dept(self,dept):
        self.__dept=dept
    def set_job(self,job):
        self.__job=job

    def get_name(self):
        return self.__name
    def get_idno(self):
        return self.__idno
    def get_dept(self):
        return self.__dept
    def get_job(self):
        return self.__job

    