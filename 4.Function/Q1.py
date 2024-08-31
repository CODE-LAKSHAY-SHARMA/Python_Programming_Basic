"""
make a function which has 5 interger parameter as a subject .and return true if pass
else return fail
"""


def marks(m1: int, m2: int, m3: int, m4: int, m5: int) -> bool:
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5
    # direct method to print
    return percentage >= 33
    # if percentage < 33:
    #     return False
    # return True


x = marks(70, 80, 90, 45, 2)
print(x)
