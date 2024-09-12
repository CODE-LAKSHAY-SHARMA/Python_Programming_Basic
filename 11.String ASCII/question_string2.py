"""
PROBLEM : SWAP CASE
convert the string word lower to upper and upper to lower and dont change 
other symbols or special character 
"""

str = "ajksda aKKFGNWE 2$@# KNDNLK 4523"
# str ke ander change nhi kar sakte hai, immutable hai
# to new variable banana padega

result = ""
for ch in str:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        result = result + chr(ascii - 32)
    elif ascii >= 65 and ascii <= 90:
        result = result + chr(ascii + 32)
    else:
        result = result + ch
print(result)
