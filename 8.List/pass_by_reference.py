"""
Printing a list using LIST as agrument in it
"""

# def printlist(lst: list) -> None:
#     print(lst)


# my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]
# printlist(my_list)


# PASS BY REFERENCE :->  address change nhi hoga , sirf value change hogi
# yeh sirf mutable data structure par work karega


def printlist(lst: list) -> None:
    lst[0] = 100


my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]
print(my_list)
printlist(my_list)
print(my_list)
