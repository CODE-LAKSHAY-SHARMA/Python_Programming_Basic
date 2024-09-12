"""
hashable thing : woh thing jo immutable hoti hai
eg :  int, string, tuples
"""

print(hash("lakshay"))
print(hash((1, 2, 3)))


set1 = {45, "lakshay", "sharma", (2, 3, 4)}
print(set1)  # tuple pass ho rha hai set ke ander concept of hashable
