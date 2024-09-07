"""
DEEP COPY 
"""

from copy import deepcopy

a = [1, 2, 3, [100, 200], 4, 5, 6]

b = deepcopy(a)  # DEEPCOPY use kar leya direct library m se
print(f"id(A)-> {id(a)}")
print(f"id(B)-> {id(b)}")

print(f"a=>{a}")
print(f"b=>{b}")


b[0] = 100
b[3][0] = 999
print(f"a=>{a}")
print(f"b=>{b}")
