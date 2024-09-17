"""
Print the maximum marks in the given dictionary , after printing the maximum marks
print the whose marks are maximum  along with marks. 
"""

from typing import List, Dict


def display_details1(my_dict: Dict[str, List[int]]) -> None:
    maximum = 0
    maximum_student_name = ""
    for name, marks in my_dict.items():
        total = 0
        for i in range(0, len(marks)):
            total = total + marks[i]
            if total > maximum:
                maximum = total
                maximum_student_name = name
    print(f"Maximum marks is  {maximum}")
    print(f"Maximum marks of student {maximum_student_name} is  {maximum}")


my_dict = {
    "lakshay": [56, 78, 56],
    "sanjay": [90, 65, 11, 44, 66],
    "aman": [81, 51, 53, 12],
    "atul": [66, 77, 87, 12, 55],
    "abhishek": [77, 98, 96],
}

display_details1(my_dict)
