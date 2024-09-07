my_list = [54, 5, 23, 5, 11, 21, 122, 99, 80]

n = len(my_list)
# Iteration by index Solution
total = 0
for i in range(0, n):
    total = total + my_list[i]
print(total)

# iteration by Value solution
total2 = 0
for i in my_list:
    total2 = total2 + i
print(total2)
