"""
Question2 : count the number of upper letter in a given string
"""

my_string = "lkdashdHIHBSa5435kljand&%@!4fjksBJAKkfb234%$"
count = 0
count1 = 0
# for ch in my_string:
#     ascii_code = ord(ch)
#     if ascii_code >= 97 and ascii_code <= 122:
#         count = count + 1
#     elif ascii_code >= 65 and ascii_code <= 90:
#         count1 = count1 + 1

# OR EASY WAY TO SOLVE THE PROBLEM
for ch in my_string:
    if "a" <= ch <= "z":
        count = count + 1
    elif "A" <= ch <= "Z":
        count1 = count1 + 1

print(f"Total lowercase Letter in string :{count}")
print(f"Total uppercase Letter in string :{count1}")
