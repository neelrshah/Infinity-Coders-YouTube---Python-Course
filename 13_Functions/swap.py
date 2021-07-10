# Function With arguments and return value:

# def swapNum(a,b):
#     print("Before SWapping:", a, b)
#     a,b = b,a
#     return a,b

# a,b = swapNum(5,10)
# print("After Swapping ",a,b)


# Function With arguments and without return value:

# def swapNum(a,b):
#     print("before swapping ",a,b)
#     a,b = b,a
#     print("After swaping ",a,b)

# swapNum(5,10)




# Functions Without arguments and with return value:

# def swapNum():
#     a = 5
#     b = 10
#     print("Before swapping " ,a,b)
#     a,b = b,a
#     return a,b

# a,b = swapNum()
# print("After swapping ", a, b)




# Functions Without arguments and without return value:

def swapNum():
    a = 5
    b = 10
    print("Before Swapping " ,a,b)
    a,b = b,a
    print("After Swapping " ,a,b)
    
swapNum()