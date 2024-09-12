"""
write a function that remove all the duplicate charachter from a given 
string in python without using libraries of python

"""

str = "programming clasess"

result = ""
for ch in str:
    if ch not in result:
        result = result + ch
print(result)
