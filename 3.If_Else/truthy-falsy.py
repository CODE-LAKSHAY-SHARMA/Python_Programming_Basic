# type casting  :  2 type
# 1. implicit type casting
# 2. explicit type casting

# Explicit conversion  :  agar hum jaan mujhkar data type convert karte hai tab usko explict conversion
num = int("100")
print(type(num))

# implicit conversion :  aapne aap conversion karna internally
age = 45

if 88:
    print("adult")
else:
    print("child")


###
"""
truthy value :  1,5,-9,100  etc all give  Truthy

falsy  :  Only 0  

float  :  1.1, 5.22, 0.0002 etc are consider in truthy
0.00 or 0 are falsy

string  :   "abc", "123"," ","."  etc are consider in truthy
"" blank string conside in the falsy 

"""

if 88:
    print("adult")
else:
    print("child")

name = "lakshay"
if name:
    print("YES")
else:
    print("NO")


name = ""  # blank string are consider as falsy statement give false answer
if name:
    print("YES")
else:
    print("NO")

# practical case in list data structure
my_list = [1, 2, 3, 4]
if my_list:  # or len(my_list)>0
    print("YES")
else:
    print("No")
