# default parameters

# required vs optional parameters


def marks(a, b, c=0, d=0, e=0):
    total = a + b + c + d + e
    print(f"The total marks is = {total}")
    percentage = total / 5
    print(f"Percentage is = {percentage}")


marks(10, 20)  # passing only 2 values in 5 parameter function
