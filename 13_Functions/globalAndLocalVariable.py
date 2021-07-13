# Global Variable & Local Variable 

# s = "Global"

# def scope():
#     x = "Local"
#     print("Inside a function")
#     print(s)
#     print(x)

# scope()

# print(x)
# print(s)


#Global keyword

a = 5
b =10
sum = 0

def add():
    global sum
    sum = a+b
    print(sum)

add()
print(sum)
