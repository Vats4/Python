a = [59, 68, 100, 5, "Vats", True, 55.556, "Code"]
# Ask a number from user
# Print yes if number exists in lists else print no

num = int(input("Enter a number= "))
"""
if num in a:
    print("yes")
else:
    print("no")
    """
if a.count(num) > 0:
    print("yes")
else:
    print("no")
