"""
Print in this format

lakshay has scored ={marks}
sanjay has scored ={marks}..etc

"""

from typing import List, Dict


# def display_details(my_dict: Dict[str, List[int]]) -> None:
#     for name, marks in my_dict.items():
#         print(f"{name} has scored = {sum(marks)}")


# without using inbuilt function
def display_details(my_dict: Dict[str, List[int]]) -> None:
    for name, marks in my_dict.items():
        total = 0
        # for i in marks:
        #     total += i
        for i in range(0, len(marks)):
            total = total + marks[i]
        print(f"{name} has Scored {total}")


# OTHER WAY WITHOUT USING ANY METHODS OF DICTIONARY


def display_details1(my_dict: Dict[str, List[int]]) -> None:
    for key in my_dict:
        total = 0
        for i in range(0, len(my_dict[key])):
            total = total + my_dict[key][i]
        print(f"{key} has Scored {total}")


my_dict = {
    "lakshay": [56, 78, 56, 67, 89],
    "sanjay": [90, 65, 11, 44, 66],
    "aman": [81, 51, 53, 12, 55],
    "atul": [66, 77, 87, 12, 55],
    "abhishek": [77, 98, 96, 41, 100],
}


display_details1(my_dict)
