""" Use the __init__() function to assign values to object properties,
    or other operations that are necessary to do when the object is being.
    
    Objects can also contain methods.
    Methods in objects are functions that belong to the object.
    
    The self parameter is a reference to the current instance of the class,
    and is used to access variables that belong to the class."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is "+self.name)


p1 = Person("John", 36)
p1.myfunc()
