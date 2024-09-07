"""
list comprhension

i-> 1 to 10

1 3 5 7 0-> ODD
2 4 6 8 -> EVEN
"""

# print even number
my_list = ["EVEN" if i % 2 == 0 else "ODD" for i in range(1, 11)]
print(my_list)

my_list1 = ["EVEN" if i % 2 == 0 else i for i in range(1, 11)]
print(my_list1)
