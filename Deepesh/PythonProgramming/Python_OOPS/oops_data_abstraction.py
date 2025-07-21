"""
# Abstraction  :  When we show overview information about any application or product and hide the internal information
 architecture then it is called abstraction.
"""
from abc import ABC, abstractmethod

# abstract
class animal(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def breed(self):
        pass


class Dog(animal):

    def name(self):
        print("Sheru")

    def voice(self):
        print("Barking")

    def breed(self):
        print("German Shefered")


class Cat(animal):

    def name(self):
        print("Jenny")

    def voice(self):
        print("Miu")

    def breed(self):
        print("Italian breed")


obj = Dog()
obj.name()

obj2 = Cat()
obj2.voice()


#str.upper()