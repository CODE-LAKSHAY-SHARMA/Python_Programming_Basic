marks = {
    "history": 78,
    "science": 80,
    "math": 76,
    "english": 55,
    "hindi": 90,
}

print(marks)


# marks.clear()

# print(marks["history"])
# print(marks.get("history"))
# other way of above , if we enter wrong keys , then return 0 rather than error

print(marks.get("histttory", 0))


# marks.pop("hindi")
# print(marks)

# OTHERWAY OF DECLARING THE DICTIONARY
from typing import Dict

marks1: Dict[str, int] = {
    "history": 78,
    "science": 80,
    "math": 76,
    "english": 55,
    "hindi": 90,
}
print(marks1)

# UPDATE METHOD IN DICTIONARY
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 1}

dict1.update(dict2)  # dict 2 ki saari value one m aajata

print(dict1)
