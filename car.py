class Car:
    def __init__ (self,model,make,speed):
        self.__model=model
        self.__make=make
        self.__speed=speed=0
    
    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed
    


