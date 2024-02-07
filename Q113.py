"""
Write a python code to find the occurrance of each element in a list 
and print the element with the highest occurrance
"""

my_list = [10, 10, 20, 20, 100, "Vats", "Pagal"]
result = []

for num in my_list:
    if num not in result:
        result.append(num)

highest_occ_element = 0
highest_occurrance = 0

for num in result:
    c = my_list.count(num)
    if c > highest_occurrance:
        highest_occurrance = c
        highest_occ_element = num
print(
    f"Highest occurrance element is {highest_occ_element} and it occurs {highest_occurrance} times."
)
