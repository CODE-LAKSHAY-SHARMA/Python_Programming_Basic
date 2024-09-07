"""
membership operator

IN 

NOT IN
"""

# it always return true or false

list1 = [5, 8, 12, 11, 9, 78, 55, 12, 99, 111]

print(8 in list1)


# Print the new list which remove all the duplicate element in the given list
list1 = [5, 8, 8, 6, 12, 11, 12, 78, 55, 12, 78, 111]
result = []

for num in list1:
    if num not in result:
        result.append(num)
print(list1)
print(result)

# or other approach

list12 = [5, 8, 8, 6, 12, 11, 12, 78, 55, 12, 78, 111]
result1 = []

for num in list12:
    if result1.count(num) == 0:
        result1.append(num)
print(list12)
print(result1)
