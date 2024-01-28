"""
Write a program that takes three numbers as input and determines
the largest one using nested if-else statements. Make sure all 3 numbers
entered by user are different.
"""

num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
num3= int(input("Enter the third number: "))

if num1==num2 or num1==num3 or num2==num3:
        print("Please make sure all three numbers are different ")


if num1!=num2 and num1!=num3 and num2!=num3:
        if num1>num2 and num1>num3:
                print(f"The greatest number is {num1}")
        elif num2>num3 and num2>num1:
                print(f"The greatest number is {num2}")
        elif num3>num2 and num3>num1:
                print(f"The greatest number is {num3}")
  