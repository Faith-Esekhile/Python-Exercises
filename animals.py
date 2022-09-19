class Mammal:
    def __init__(self,species):
        self.__species=species
    def show_species(self):
        print("i am a ",self.__species)
    def make_sound(self):
        print("grrrrrrrr")
    

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self,"dog")
    def make_sound(self):
        print("woof! woof!")

class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self,"Cat")
    def make_sound(self):
        print("meow")
    

