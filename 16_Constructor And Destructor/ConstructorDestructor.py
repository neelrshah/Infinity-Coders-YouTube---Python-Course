# Constructor
# class Myclass:
    # def __init__(self):
    #     print("inside a constructor")

#     def __init__(self,a,b):
#         sum = a + b
#         print("inside paramaterised constructor")
#         print(sum)

# c = Myclass(5,10)

# Destructor

class Myclass:
    def __init__(self, a, b):
        sum = a + b
        print("inside paramaterised constructor")
        print(sum)

    def __del__(self):
        print("destructor")

c = Myclass(5, 10)
