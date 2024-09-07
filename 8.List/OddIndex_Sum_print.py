"""
Tell me the sum of all element in odd index
"""

my_list = [54, 5, 23, 5, 11, 21, 122, 99, 80]

n = len(my_list)
total = 0

for i in range(0, n):
    if i % 2 != 0:
        total = total + my_list[i]
print(total)
