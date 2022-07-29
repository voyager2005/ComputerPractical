"""
Write a program to enter 2 integers ,1 arithmetic operator and display
the computed result by using some user defined functions and elif
statement.
"""
import math


# user defined functions
def compute(x, y, operator):
    result = 0
    if operator == '+':
        result = addition(x, y)
    elif operator == '-':
        result = subtraction(x, y)
    elif operator == '*':
        result = multiplication(x, y)
    elif operator == '/':
        result = division(x, y)
    elif operator == '^':
        result = exponent(x, y)
    elif operator == '%':
        result = modulus(x, y)

    return result


def addition(x, y):  # adding the two numbers and returning the value
    return x + y


def subtraction(x, y):  # subtracting the two numbers and returning the value
    return x - y


def multiplication(x, y):  # multiplying the two numbers and returning the value
    return x * y


def division(x, y):  # dividing the two numbers and returning the value
    return x / y


def exponent(x, y):  # power of two numbers x^y and returning the value
    return math.pow(x, y)


def modulus(x, y):  # modulus of the two numbers and returning the value
    return x % y


# __main__
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
arithmetic_operator = input("Please enter the arithmetic operator: ")
answer = compute(num1, num2, arithmetic_operator)

# displaying the answer
print(num1, " ", arithmetic_operator, " ", num2, " = ", answer)
