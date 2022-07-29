"""
Prepare a menu-driven program by creating functions
1.calculate the area of circle
2.calculate the area of rectangle
3.calculate the area of a square
"""
import math

# declaring and initializing the values
area = 0.0

# reading the choice from the user
choice = input("1 for AREA OF CIRCLE\n"
               "2 for AREA OF RECTANGLE\n"
               "3 for AREA OF SQUARE\n"
               "Please enter your choice: ")

if choice == '1':
    # calculating the area of a circle
    r = int(input("\nPlease enter the RADIUS of the CIRCLE: "))
    area = math.pi * math.pow(r, 2)
    print("AREA of the CIRCLE is: ", area)
elif choice == '2':
    # calculating the area of a rectangle
    l = int(input("\nPlease enter the LENGTH or the RECTANGLE: "))
    b = int(input("Please enter the BREADTH of the RECTANGLE: "))
    area = l * b
    print("AREA of the RECTANGLE is: ", area)
elif choice == '3':
    # calculating the area of a square
    a = int(input("\nPlease enter the length of a single side of the SQUARE: "))
    area = a * a
    print("AREA of CIRCLE is: ", area)
else:
    print("INVALID CHOICE")
