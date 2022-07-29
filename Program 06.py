"""
write a program to read 4 bytes from a text file and then read the
Entire contents from the file.
"""

# creating the file object using .open() function
MyFile = open("sample.txt", 'r')

# reading the first 4 bytes of the file and displaying them
x = MyFile.read(4)
print(x)

# reading the remaining file and displaying it
x = MyFile.read()
print(x)
