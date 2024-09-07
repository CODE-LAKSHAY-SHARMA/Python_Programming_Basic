"""
list slicing 
"""

# to fetch the first 4 element in the given element in list
list1 = [534, 653, 12, 14, 11, 55, 3]
print(f"Original list=>{list1}")
x = []
for i in range(0, 4):
    x.append(list1[i])
print()
print(f"FETCHED LIST through append method=>{x}")
print()
# alternative: LIST SLICING

x1 = list1[0:4]
print(f"SLICED LIST=>{x1}")
print()


b = list1[:]
print(b)


# medium of the element print karna hai

list2 = [534, 653, 12, 14, 11, 55, 3]
list2_length = len(list2)

print(list2[0 : list2_length // 2])


# Negative index
list1 = [534, 653, 12, 14, 11, 55, 3]
# x = list1[::-1]
# x = list1[-5:-1]
x = list1[-2:-1]
print(x)
