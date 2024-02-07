"""
Make a list. Then ask a number from user. 
If number exists in that list then print the position of the element else print -1.
"""

my_list = [10, 10, 20, 20, 100]

value = int(input("Enter a value = "))

if value in my_list:
    index = my_list.index(value)
    print(f"Index= {index}")
else:
    print(-1)
