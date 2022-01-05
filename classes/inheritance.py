# Prevents code duplication and allows us to reuse code

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")
# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


dog = Mammal()
dog.eat()
print(dog.age)

print(isinstance(dog, Mammal))
print(issubclass(Mammal, Animal))
