"""
Q39.
Write a program that checks if a given year is a leap year.Leap years are divisible by 4,
 but not by 100 unless they are also divisible by 400.
"""

Year= int(input("Enter a year"))

#To check if a year is a leap year.
if Year%4 ==0:
    print(f"Year {Year} is a Leap year.")

elif Year%100==0 and Year%400==0:
    print(f"Year {Year} is a Leap year.")

else:
    print(f"Year {Year} is not a leap year.")
