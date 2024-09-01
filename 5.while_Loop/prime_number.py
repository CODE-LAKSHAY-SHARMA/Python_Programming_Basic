# prime  number
# number divisible by 1 and itself


def factor(x: int) -> int:
    i = 1
    count = 0
    while i <= x:
        if x % i == 0:
            count = count + 1
        i = i + 1
    return count


def prime(num: int) -> bool:
    factors = factor(num)
    if factors == 2:  # jiske sirf 2 factor hai woh prime hai othewise False
        return True
    else:
        return False


val = prime(11)
print(val)
