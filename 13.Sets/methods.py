"""
SET METHODS 
"""

set1 = {1, 2, 3, 4, 5, 4, 3, 6, 8, 9, 1}
print(set1)
set1.add(100)  # unorder hai, kahi bhi add ho jaayega
print(set1)


set1.remove(5)
print(set1)


# set1.clear()  # set become empty
# print(set1)

another = set1  # address copy hota hai , value change nhi hoti
print(another)
print(set1)
