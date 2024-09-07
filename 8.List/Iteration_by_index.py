my_list = [54, 5, 23, 5, 11, 21, 11222, 998, 800]

# Iteration to fetch the element in the list
# Iterate by Index
n = len(my_list)
for i in range(0, n - 1):
    print(my_list[i], end=" ")
print()
# print reverse

for i in range(n - 1, -1, -1):
    print(my_list[i], end=" ")
