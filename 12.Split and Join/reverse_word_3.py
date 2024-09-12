"""
Reverse the each word of the sentence 

INPUT  
my_string="python is a good language"

OUTPUT
eguagnal doog a si nohtyp
"""

my_string = "python is a good language"
words = my_string.split()  # convert the string into list
# 1 approach
words.reverse()
print(" ".join(ch[::-1] for ch in words))

# # 2nd Approach
# print(" ".join(ch[::-1] for ch in words[::-1]))
