"""
A student will not be allowed to sit in exam if his/her attendance is less then 75%.
Take following input from user:
.Number of classes held
.Number øf classes attended

1 Print percentage of class attended
2 Print if student is allowed to sit in the exam or not.
"""
num_of_classes_held=int(input("Enter classes held: "))
num_of_classes_attended=int(input("Enter classes attended: "))

class_per=(num_of_classes_attended/num_of_classes_held)*100

print(f"Percentage of class attended = {class_per:.2f}% ")
if class_per>=75:
    print("Yes you can sit in the exam")
else:
    print("No, YouCannot sit in the exam")








