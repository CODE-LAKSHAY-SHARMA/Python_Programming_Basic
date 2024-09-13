marks = {
    "history": 78,
    "science": 80,
    "math": 76,
    "english": 55,
    "hindi": 90,
}
print(marks.keys())
print(marks.values())
print(marks.items())  # give key value pair format

result = marks.items()
print(list(result)[0][1])  # set ke ander indexing nhi hoti hai , will not works

# otherway ( BEST WAY)
print(result)
for k, v in result:
    print(f"KEY => {k} ,VALUE => {v}")
