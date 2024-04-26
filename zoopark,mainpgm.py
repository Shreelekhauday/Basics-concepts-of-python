#abstract pgm
from zoopark import abstractpets

class Animal(abstractpets):
    def display_details(self):
        print("Animal details:")
        print("color:",self.color)
        print("number of types:",self.num_types)
        print("sound:",self.sound)

class Birds(abstractpets):
    def display_details(self):
        print("Birds details")
        print("color:",self.color)
        print("number of types:",self.num_types)
        print("sound:",self.sound)

class Shree(abstractpets):
    def display_details(self):
        print("Shree details")
        print("color:",self.color)
        print("number of types:",self.num_types)
        print("sound:",self.sound)

#parent pgm
from abc import ABC, abstractmethod
class abstractpets(ABC):
    def __init__(self,color,num_types,sound):
        self.color=color
        self.num_types=num_types
        self.sound=sound
@abstractmethod
def display_details(self):
    pass


#main pgm
from abstractpets import Animal,Birds,Shree

def main():
    animal=Animal(color= "Orange",num_types= 7,sound ="large")
    birds=Birds(color= "Green",num_types= 5,sound="medium")
    shree=Shree(color ="Gold",num_types= 3,sound="loud")

    animal.display_details()
    print("\n")
    birds.display_details()
    print("\n")
    shree.display_details()


if __name__=="__main__":
    main()
