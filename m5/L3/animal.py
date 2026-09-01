class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print(f"{self.name} made a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def show_breed(self):
        print(f"{self.breed} is breed")
    def make_sound(self):
        print(f"{self.name} said woof")

dog1 = Dog("frfr", "golden_retriever")
dog1.make_sound()
dog1.show_breed()