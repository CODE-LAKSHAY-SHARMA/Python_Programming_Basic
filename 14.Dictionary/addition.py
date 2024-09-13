from typing import Dict

marks1: Dict[str, int] = {
    "history": 78,
    "science": 80,
    "math": 76,
    "english": 55,
    "hindi": 90,
}

# english ke marks 98 karne hai and 55 ko replace karke
# 1st approach
marks1.update({"english": 98})
print(marks1)

# 2nd Approach
marks1["hindi"] = 99
print(marks1)
