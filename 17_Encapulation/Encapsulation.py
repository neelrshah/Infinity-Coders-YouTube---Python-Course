
class MyCLass:
    a = 10
    __b = 20

    def display(self):
        print(self.a)
        print(self.__b)

o =MyCLass()
o.display()
print(o.__b)
    