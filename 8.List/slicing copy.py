"""
list slicing 
"""

list1 = [534, 653, 12, 14, 11, 55, 3]
print(f"My list =>{list1}")
print(f"My list ID =>{id(list1)}")

print()
b = list1[:]  # ID will change after giving colon
# this is same as .copy method alternative
print(f"My list =>{b}")
print(f"My list ID =>{id(b)}")


# same list ke ander change karna hai toh
# list1[:]=list1[0:4]
# agar dusre list m value assign karni hai toh
# list1=list1[0:4]
