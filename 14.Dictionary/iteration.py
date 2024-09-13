marks = {
    "history": 78,
    "science": 80,
    "math": 76,
    "english": 55,
    "hindi": 90,
}

for k in marks:  # by default we get KEYS as answer
    print(k)
    print(marks[k])

# calculate the total of every marks
# 1 APPROACH

total = 0
for k in marks:
    total = total + marks[k]
print(f"total marks is {total}")

# 2nd APPROACH
sum1 = 0
for i in marks.values():
    sum1 = sum1 + i
print(sum1)
