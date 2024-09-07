"""
List Methods/Function :  
"""

# list1 = [5, 6, 7, "lakshay", 77.87, True, False]
# print(list1)
# list1.append(100)
# print(list1)


# Other way of printing the list

# list1: list = [5, 6, 7, "lakshay", 77.87, True, False]
# list1.append(2999)
# print(list1)


# Now we want only integer data type to be store in the list rest cannot
from typing import List

list1: List[int] = [5, 6, 7, 88]
list1.append(2999)
print(list1)
