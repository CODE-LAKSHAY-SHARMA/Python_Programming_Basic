"""
even number +1 and odd number -1 in a given list we have to perform that
"""

my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]

# by value  or by index we are updating the element

# By Index
n = len(my_list)
for i in range(n):
    if my_list[i] % 2 == 0:
        my_list[i] = my_list[i] + 1
    else:
        my_list[i] = my_list[i] - 1
print(my_list)
