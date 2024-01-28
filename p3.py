"""
Ask physics and chemistry marks from user
Print PASS, if student is passes in both subjects
Else print FAIL
"""
P_marks= int(input("Enter physics marks: "))
C_marks= int(input("Enter chemistry marks: "))

if P_marks>=33 and C_marks>=33: 
    print("PASS")
else:
    print("FAIL")

