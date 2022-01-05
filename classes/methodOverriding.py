# Method Overriding - extending or replacing methods deifined in the base class

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")
# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def __init__(self):
        self.weight = 2
        super().__init__()  # to access mothods from the base class


class Fish(Animal):
    def swim(self):
        print("swim")
