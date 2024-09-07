my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]

# by value  or by index we are updating the element

# By Index
n = len(my_list)
for i in range(n):
    if my_list[i] % 2 == 0:
        my_list[i] = my_list[i] + 5
print(my_list)
