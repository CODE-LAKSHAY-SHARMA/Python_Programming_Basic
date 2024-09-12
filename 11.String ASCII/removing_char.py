"""
Remove all the symbols, digits, spaces from the string

Example:
str=""a$b^&c9D  e.f$%g"

Result:
"abcDefg"
"""

str = "a$b^&c9D  e.f$g"
result = ""
for ch in str:
    ascii = ord(ch)
    if (ascii >= 97 and ascii <= 122) or (ascii >= 65 and ascii <= 90):
        result = result + ch
    else:
        continue
print(result)
