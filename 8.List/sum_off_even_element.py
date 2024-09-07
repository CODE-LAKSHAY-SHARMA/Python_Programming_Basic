"""
print the sum of even numbers in the given list
"""

my_list = [54, 5, 23, 5, 11, 21, 122, 99, 80]

n = len(my_list)
total = 0

for i in my_list:
    if i % 2 == 0:
        total = total + i
print(total)


# OR iterative through index

total2 = 0
for i in range(0, n):
    if my_list[i] % 2 == 0:
        total2 = total2 + my_list[i]
print(total2)
