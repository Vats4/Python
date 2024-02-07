"""
Q115.
Write a program that has two lists and 
make a new list that contains only the common elements between them without duplicates.
"""

list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]
common_list = []

for element in list_1:
    if element in list_2 and element not in common_list:
        common_list.append(element)


print(f"Common elements: {common_list}")
