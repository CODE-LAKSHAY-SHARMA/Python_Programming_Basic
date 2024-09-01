def factor(x: int) -> int:
    i = 1
    count = 0
    while i <= x:
        if x % i == 0:
            count = count + 1
        i = i + 1
    return count


val = factor(20)
print(val)
