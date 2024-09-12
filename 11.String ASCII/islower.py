"""
Print true if the below string is a lower case else False 
"""

# print(my_string.islower())  # direct method use nhi karna hai


# agar ek bhi character lower hai toh lower hoga TRUE hoga


def islower(my_string: str) -> bool:
    is_lower = False
    is_upper = False
    for ch in my_string:
        if "a" <= ch <= "z":
            is_lower = True
        elif "A" <= ch <= "Z":
            is_upper = True
    if is_lower == True and is_upper == False:
        return True
    return False


my_string = "askasSD%#$@(asfdas)A"
print(islower(my_string))
