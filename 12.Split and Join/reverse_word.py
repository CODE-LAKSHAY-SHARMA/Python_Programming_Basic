"""
Reverse the word 

INPUT  
my_string="python is a good language"

OUTPUT
language good a is python
"""

my_string = "python is a good language"
words = my_string.split()  # convert the string into list
print(words)

# 1 approach
# words.reverse()
# print(words)

# 2nd approach(slicing karke)
words = words[::-1]
print(words)


# ek baar ulta ho gaya toh join karna hai
# to list ko join karke string banana hai toh .join() use karnenge

result = " ".join(ch for ch in words)
print(result)
