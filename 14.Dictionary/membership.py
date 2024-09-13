from typing import Dict

marks1: Dict[str, int] = {
    "history": 78,
    "science": 80,
    "math": 76,
    "english": 55,
    "hindi": 90,
}


print(80 in marks1)  # this will give false as it return complete key and value
print(80 in marks1.values())  # return only values in dictionary
