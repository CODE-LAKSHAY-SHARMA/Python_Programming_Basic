# Now we want only integer data type to be store in the list rest cannot
from typing import List

list1: List[int] = [5, 6, 7, 88, 100, 1150]
print(list1)
list1.extend([9, 10, 11])  # list got added at the end
print(list1)

# COUNT METHODS
print(list1.count(100))  # count will count the occurence

# INDEX(pass the value):  this will help to find the index position of the value

y = list1.index(1150)  # will give the index position of the value
print(y)

# SORT method in list
list1.sort()
print(list1)

# SORT METHOD ( reverse=True)
list1.sort(reverse=True)  # print in descending order
print(list1)
