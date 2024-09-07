"""
Ask a number from user , enter element user ask number
and at last print the number in the list

"""

from typing import List


def create_list(length: int) -> List[int]:

    list1 = []
    for i in range(1, length + 1):
        a = int(input(f"Enter {i} number:"))
        list1.append(a)
    return list1


user = int(input("enter the number"))
val = create_list(user)
print(val)
