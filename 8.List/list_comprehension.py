"""
list comprhension
"""

# basic apprach to create a list with even number and print it

# list1 = []
# for i in range(0, 101):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)

# another way to print the above code in one line

my_list = [i for i in range(0, 101) if i % 2 == 0]
print(my_list)

# print [-1,-1,-1,-1,-1]
a = [-1 for x in range(0, 5)]
print(a)
