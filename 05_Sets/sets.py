# set basics
    # creating a set

# s = {1,2,3,4}
# s1 = set()

#     # printing a set

# print(s)
# print(s1)

    # duplicate elements in set

# s = {1,2,3,2,3}
# print(s)




# set methods

# add(), remove(), clear(), difference(), intersection(), symmetric_difference()
# union(), issubset(), pop()


# s = {1,2}
# s.add(3)
# print(s)

# s.remove(2)
# print(s)

# # s.clear()
# # print(s)

# s.pop()
# print(s)


s = {1,2,3,4}
s2 = {2,3,5,6,7}

print(s.union(s2))
print(s.intersection(s2))
print(s.difference(s2))
print(s.symmetric_difference(s2))
