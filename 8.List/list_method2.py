"""
List Methods/Function :  
"""

# Now we want only integer data type to be store in the list rest cannot
from typing import List

list1: List[int] = [5, 6, 7, 88]
print(list1)
list1.insert(3, 100)
print(list1)

list1.insert(-1, 250)
print(list1)


# Remove the element (POP)-> this will return the element also
x = list1.pop()  # Delete by index
print(x)

# del command
del list1[2]  # 3rd index will get delete
print(list1)

# Remove
list1.remove(100)  # delete by value
print(list1)
