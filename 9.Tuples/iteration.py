"""
Iteration in tuples
"""

my_tuple = (1, 2, 3, 4, "lakshay", True, False)
n = len(my_tuple)

for i in range(n):
    print(my_tuple[i], end=" ")
print()
# other way by value
for i in my_tuple:
    print(i, end=" ")
