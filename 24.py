"""
Write a program that tales a character as input and prints whether its positive, negative.(Consider 0 as positive)
"""
Character= str(input("Enter a character"))

if Character == "a" or Character == "e" or Character== "i" or Character=="o" or Character== "u":
    print(f" {Character} is a vowel.")

else:
    print(f" {Character} is a consonant ")

