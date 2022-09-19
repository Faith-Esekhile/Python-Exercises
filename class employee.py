class Employee:
    def __init__(self,name,ID,department,job_title):
        self.__name=name
        self.__ID=ID
        self.__dept=department
        self.__job=job_title

    def set_department(self,department):
        self.__dept=department
    def set_job_title(self,job_title):
        self.__job=job_title
    def get_name(self):
        return self.__name
    def get_ID_number(self):
        return self.__ID
    def get_department(self):
        return self.__dept
    def get_job_title(self):
        return self.__job
    def __str__(self):
        return "name"+self.__name + "\n" \
                "ID NUMBER:"+ str(self.__ID) + "\n" \
                "department:"+self.__dept+"\n"+\
                "job title:" + self.__job
susan = Employee("susan meyer",47899,"accounting","vice president")
mark = Employee("mark jones",39119,"IT","programmer")
joy=Employee("joy rogers",81774,"manufacturing","engineer")
tick=Employee("the tick",99991,"justice","superhero")

print(susan,end="\n\n")
print(mark, end="\n\n")
print(joy,end="\n\n")
print(tick)

