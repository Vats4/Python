"""
Q110.
Make a list of your own. And remove all the duplicates element from that list.
"""

my_list = [10, 10, 20, 20, "Vats", 44.65678, "Vats", "stupid", "stupid", True, False]
result = []

for num in my_list:
    if num not in result:
        result.append(num)

print(result)
