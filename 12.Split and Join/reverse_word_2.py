"""
Reverse the each word of the sentence 

INPUT  
my_string="python is a good language"

OUTPUT
nohtyp si a doog eguagnal
"""

my_string = "python is a good language"
words = my_string.split()  # convert the string into list
print(words)

print(" ".join(ch[::-1] for ch in words))


# ek baar ulta ho gaya toh join karna hai
# to list ko join karke string banana hai toh .join() use karnenge

# result = " ".join(ch for ch in words)
# print(result)
