"""
Write a program to find out how many even and odd numbers are
present in a list of integers.
"""

# declaration and initialization of variables
list1 = []
odd_count, even_count = 0, 0

# reading the number of entries from the user
entries = int(input("How many numbers do you want to enter? "))

# for loop to initialize <entries> number of int values into list l
print("\nPlease enter the digits")
for i in range(0, entries):
    num = int(input("Enter the number: "))
    list1.append(num)

# iterating through each element in the list
for num in list1:

    # condition to check for even
    if num % 2 == 0:
        even_count += 1
    # condition to check for odd
    else:
        odd_count += 1

# printing the number of odd and even numbers in the list
print("\nNumber of odd numbers are: ", odd_count)
print("Number of even numbers are: ", even_count)
