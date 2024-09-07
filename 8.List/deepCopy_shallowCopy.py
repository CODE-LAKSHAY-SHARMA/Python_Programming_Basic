"""
Shallow Copy and Deep Copy concept in list 
"""

a = [1, 2, 3, 4, 5, 6]

b = (
    a.copy()
)  # this is not the good method to save the duplicate list, humne sirf memory copy kari hai
print(f"id(A)-> {id(a)}")
print(f"id(B)-> {id(b)}")

print(f"a=>{a}")
print(f"b=>{b}")

# and jab mane b ki index position ki value change kari toh a ki bhi value change ho gai hai
b[0] = 100
print(f"a=>{a}")
print(f"b=>{b}")
# NOTE that value of A list also changes at index position 0,
# therefore to avoid this we use the concept of shallow copy and deep copy
# as done above

# DEEP COPY :  nested list ki ID change karna
