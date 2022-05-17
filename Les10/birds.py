import playsound, datetime as dt
from animals import Animal

class Bird(Animal):
    species = "vogel"

    def info(self):
        print("Bird")
        


class Parrot(Bird):
    species = "papegaai"

    def __age(self, birthdate):
        return dt.datetime.now().year - birthdate.year

    def __init__(self, name, birthdate, color):
        self.name = name
        self.age = self.__age(birthdate)
        self.color = color
    
    def sing(self):
        playsound.playsound("parrot.wav")
    
    def talk(self, text):
        print(self.name,"zegt",text)

    def info(self):
        print(self.name,"is een", self.species)