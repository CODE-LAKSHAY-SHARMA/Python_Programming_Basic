"""
Question 1 : tell me the string with maximum frequency there occurenance and 
character name also
"""

my_string = "ahgghtgkjdllmmmmasahhaggg"


dict = {}
for i in my_string:
    dict[i] = dict.get(i, 0) + 1  # key value pair m store kar deya
print(dict)

max_frequency = 0
max_element = 0
result = dict.items()  # yaha par item store karna hoga
for i, k in result:
    if k >= max_frequency:
        max_frequency = k
        max_element = i

print(f"The maximum frequency of element  {max_element} is {max_frequency}")
