"""
Question : count the number of small letter in a given string
"""

my_string = "lkdashdfha5435kljand&%@!4fjkskfb234%$"
count = 0
for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code >= 97 and ascii_code <= 122:
        count = count + 1
print(f"Total Lowercase Letter in string :{count}")
