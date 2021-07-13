# Class
class SmartPhone:
    def __init__(self,processor,ram,memory,price):
        self.processor = processor
        self.ram = ram
        self.memory = memory
        self.price = price

    def display(self):
        print("RAM :  " + self.ram)
        print("processor :  " + self.processor)
        print("price :  " + self.price)
        print("memory :  " + self.memory)

# Objects

note7 = SmartPhone("snapdragon","4GB","64GB","15000")
note7.display()

# Accessing elements of objects

print(note7.memory)