"""
ask 5 marks from user:
Calculate percentage and print it.

91-100 -> A grade
81-90 -> B grade
71-80 -> c grade
61-70 -> d grade
1-60 -> FAIL
Invalid
"""
maths= int(input("Enter marks in maths = "))
science= int(input("Enter marks in maths = "))
english= int(input("Enter marks in maths = "))
hindi= int(input("Enter marks in maths = "))
history= int(input("Enter marks in maths = "))

total= maths + science + english + hindi + history
percentage = (total/500)*100
print(f"percentage score = {percentage}")

if percentage >=91 and percentage<=100:
    print("A grade")
elif percentage>=81 and percentage<=90:
    print("B grade")
elif percentage>=71 and percentage<=80:
    print("C grade")

elif percentage>=61 and percentage<=70:
    print("D grade")

elif percentage>=1 and percentage<=60:
     print("FAIL")
else:
    print("Invalid Percentage")
    