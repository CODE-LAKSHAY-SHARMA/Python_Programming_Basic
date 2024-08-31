"""
Make a function name marks , it should take 5 integers as parameter, print the 
total and print the percentage
"""


def marks(a: int, b: int, c: int, d: int, e: int):
    total = a + b + c + d + e
    print(f"The total marks is = {total}")
    percentage = total / 5
    print(f"Percentage is = {percentage}")


marks(10, 20, 25, 30, 45)
