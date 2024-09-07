"""
How memory works ??
"""

# PASS BY REFERENCE : address change nhi hoga , sirf value change hogi

my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]
print(id(my_list))
print(my_list)


my_list[1] = 1000
print(id(my_list))  # we will get the same id of the above, bcox list are mutable
print(my_list)
