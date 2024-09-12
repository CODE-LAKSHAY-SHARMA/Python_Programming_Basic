"""
convert the string into uppercase without using upper() method of string
"""

str = "ajksdBJAKDkjakfjBKJ"
# str ke ander change nhi kar sakte hai, immutable hai
# to new variable banana padega

result = ""
for ch in str:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        ascii = ascii - 32
        result = result + chr(ascii)
    else:
        result = result + ch
print(result)
