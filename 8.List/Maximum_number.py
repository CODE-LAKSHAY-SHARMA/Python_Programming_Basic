"""
Find the largest/maximum element in the given list/array
"""

# BASIC /EASY APPROACH

my_list = [45, -31, 7, -5, 3, 100, 17, 19, 25, -65, 92]
maxi = float("-inf")
n = len(my_list)

for i in my_list:
    if i > maxi:
        maxi = i
print(f"Maximum number in given list is {maxi}")


# DSA approach

for i in range(n):
    maxi = max(maxi, my_list[i])
print(f"Maximum number in the array is {maxi}")
