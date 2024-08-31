#
# when we dont know the argument


# spread split
def add(n1, n2, *n3):
    print(f"n1-> {n1}")
    print(f"n1-> {n2}")
    print(f"n1-> {n3}")


add(10, 20, 30, 40, 50)  # after 20 number rest number will go to n3


# Concept of ARGS ( *num )
def diff(*n1):
    print(f"n1-> {n1}")


diff(10, 20, 30)
