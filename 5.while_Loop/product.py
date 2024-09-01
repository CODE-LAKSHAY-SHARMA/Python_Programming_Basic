"""
 print 1 to 10 total product
 1*2*3*---*9
"""

# concept of factorials


def product_of_number(num: int) -> int:
    i = 1
    total = 1
    while i <= num:
        total = total * i
        i = i + 1
    return total


a = int(input("enter number =>"))
val = product_of_number(a)
print(val)
