"""
Write a program to enter a string and check how many vowels,
consonants and special characters present in that string.
"""

# declaration and initialization of variables
vowels = 0
consonant = 0
specialChar = 0
digit = 0

# reading the string from the user and storing it in variable s
s = input("Please enter a string: ")

# len(<variable name>) function to count
# number of character in given string.
for i in range(0, len(s)):

    ch = s[i]

    if ch.isalpha():

        # To handle upper case letters
        ch = ch.lower()

        if (ch == 'a' or ch == 'e' or ch == 'i'
                or ch == 'o' or ch == 'u'):
            vowels += 1
        else:
            consonant += 1

    elif ch.isdigit():
        digit += 1
    else:
        specialChar += 1

print("Vowels:", vowels)
print("Consonant:", consonant)
print("Digit:", digit)
print("Special Character:", specialChar)
