"""
368 ke factors ka total sum calculate karna hai

"""


def factor(x: int) -> int:
    i = 1
    sum = 0
    while x >= i:
        if x % i == 0:
            sum = sum + i
        i += 1
    return sum


a = factor(368)
print(a)
