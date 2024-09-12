"""
1. SPLIT()-> convert from string to list
2. JOIN ()->  convert list to string
"""

# my_list1 = ["a", "b", "c", "d", "e"]

# result = "".join(ch for ch in my_list1)
# print(result)

my_list = [4, 5, 6, 6, "lakshay", "z", "y"]
# first convert int to str , tabhi join() chelga
print("-".join(str(ch) for ch in my_list))
