# with annotation


def average(n1: int, n2: int, n3: int, n4: int) -> float:
    total = n1 + n2 + n3 + n4
    return total / 4


def add(num1: int, num2: int) -> None:
    total = num1 + num2
    # return total  # we cannot use return here as above -> None is mention
    # we need to only print the output
    print(total)


x = average(10, 20, 30, 40)
print(x)

add(10, 20)


def concat(firstname: str, lastname: str) -> str:
    return firstname + lastname


# we can use return here as the function is returning a string
print(concat("John", "Doe"))
