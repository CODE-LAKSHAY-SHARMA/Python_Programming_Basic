def add(a, b, c):
    total = a + b + c
    return total


def add_withoutReturn(a, b, c):
    sum = a + b + c
    print(sum)


def even_odd(x):
    if x % 2 == 0:
        print("Sum is even")
    else:
        print("Sum is ODD")


x = add(34, 44, 45)
print(x)
even_odd(x)
