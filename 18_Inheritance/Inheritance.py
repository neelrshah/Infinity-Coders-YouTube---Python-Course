# Inheritance


# Single Level Inheritance

class Animal:
    def __init__(self):
        print("inside animal")

    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("inside dog")
        
    def bark(self):
        print("Dog is barking")

d = Dog()
d.bark()
d.speak()