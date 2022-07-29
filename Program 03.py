"""
Create a dictionary by using a loop.
"""

# declaration and initialization of variables
d = {}

# reading the number of dictionary elements
length = int(input("Number of elements in dictionary: "))

# loop to initialize dictionary
for i in range(0, length):
    key = input("Please enter the key: ")
    value = input("Please enter the value: ")
    d[key] = value
