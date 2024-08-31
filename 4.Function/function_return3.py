# agar koi function return karta hai toh phir usko directly print kar sakte hai
def average(n1: int, n2: int, n3: int, n4: int) -> float:
    total = n1 + n2 + n3 + n4
    return total / 4


print(average(10, 20, 30, 40))  # we dont need to store the value of return

# very important question


def sum(a, b):
    total = a + b
    print(total)


x = sum(10, 20)
print(x)
print(sum(10, 20))
