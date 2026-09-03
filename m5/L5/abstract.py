from abc import ABC, abstractmethod

class Abs(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Animal(Abs):
    def make_sound(self):
        print("It made a sound")

a = Animal()
a.make_sound()