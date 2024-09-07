"""
a list is avaiable, remove all the even number in the given list
"""

list1 = [5, 8, 12, 11, 9, 78, 55, 12]
# print(list1)

# n = len(list1)

# for i in range(0, n):
#     if list1[i] % 2 == 0:
#         list1.pop(i)

# print(list1)

# above code will error because index position change nhi ho rhi hai

# ANOTHER WAY TO APPROACH THIS PROBLEM

list1 = [5, 8, 12, 11, 9, 78, 55, 12, 99, 111]
print(list1)
result = []

for i in range(0, len(list1)):
    if list1[i] % 2 != 0:
        result.append(list1[i])
print(result)
