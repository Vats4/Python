"""
Calculate the sum of 5 subjects and Find percentage.
"""
subject1 = int(input("Enter first subject marks: "))
subject2 = int(input("Enter second subject marks: "))
subject3 = int(input("Enter third subject marks: "))
subject4 = int(input("Enter fourth subject marks: "))
subject5 = int(input("Enter fifth subject marks: "))

sum = subject1+subject2+subject3+subject4+subject5
print(f"Sum of subjects: {sum}")

percentage= float(sum*100)/500.

print(f"Percentage: {percentage}")
