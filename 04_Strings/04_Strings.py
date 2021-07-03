# String Basics

    # Creating a String

# s = "Python"

    # Printing a String

# print(s)

    # String Concatenation

# s1 = "hello"
# s2 = "world"
# print(s1 + s2)
    # Indexing and accessing elements of String

# s = "Python"
# print(s[0])
# print(s[-1])


    # Slicing of String
# s = "hello world"

# # s[start : ending : gaps]

# print(s[0:5])
# print(s[:-3])
# print(s[::2])

# in-biuld Strings functions 

# lower(), upper(), swapcase(), isupper(), islower(), capitalize(), len(),
# isdigit(), isalnum(), isalpha()


s = "python"

# print(s.upper())
# print(s.lower())
# s2 = "PytHoN"
# print(s2.swapcase())
# print(s.isupper())
# print(s.islower())
# print(s.capitalize())
# print(len(s))


s1 = "123"
s2 = "AB12"
s3 = "abc"

print(s1.isdigit())
print(s3.isalpha())
print(s2.isalnum())