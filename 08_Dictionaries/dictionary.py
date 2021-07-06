# Basic of Dictionary 

# Creating a Dictionary
# car = {
#     "name" : "BMW",
#     "color" : ["Red", "Black"]
# }

# Printing a Dictionary
# print(car)

# Accessing elements of Dictionary

# print(car["name"])
# print(car.get("name"))



# Basic in-build Functions of Dictionary

car = {
    "name" : "BMW",
    "color" : ["Red","Black"]
}

# print(car.keys())
# print(car.values())

# car["name"] = "AUDI"
# print(car)
# car.update({"name" : "BMW"})
# print(car)
# car.update({"id" : 12})
# print(car)

car.pop("color")
print(car)

car.clear()
print(car)