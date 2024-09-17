"""
Question 1 : Tell me the maximum frequency in the given list
Question 2:  Also tell me the whose frequency is most 
"""

my_list = [4, 5, 8, 8, 8, 6, 8, 9, 5, 5, 3, 1, 7, 8, 9]

dict = {}
for i in my_list:
    dict[i] = dict.get(i, 0) + 1  # key value pair m store kar deya
print(dict)

# now to check the maximum frequency
# ans = 0

# for i in dict.values():
#     if i >= ans:
#         ans = i

max_frequency = 0
max_element = 0
result = dict.items()  # yaha par item store karna hoga
for i, k in result:
    if k >= max_frequency:
        max_frequency = k
        max_element = i

print(f"The maximum frequency of element  {max_element} is {max_frequency}")
