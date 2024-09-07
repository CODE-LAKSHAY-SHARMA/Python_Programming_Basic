list1 = [5, 8, 12, 11, 9, 78, 55, 12]
print(list1)
result = []

for i in range(0, len(list1)):
    if list1[i] % 2 != 0:
        result.append(list1[i])
print(result)
