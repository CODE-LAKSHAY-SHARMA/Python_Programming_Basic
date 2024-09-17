details = {
    "lakshay": {"age": 23, "gender": "male", "marks": [3, 6, 77, 8, 3], "adult": True},
    "muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [56, 74, 41, 53],
        "adult": False,
    },
    "Nihar": {"age": 26, "gender": "male", "marks": [56, 88, 11, 54, 3], "adult": True},
}
# # Question 1 : what is the gender of muskan : access that

# print(details["muskan"]["gender"])

# print(details["muskan"]["marks"][-1])


"""
Question 2
Print the name of person who is ADULT i.e adult =True and print the age also
"""
for name, info in details.items():
    if info["adult"] == True:
        print(name, info["age"])

"""
Question 3
print
lakshay has score marks
muskan has score marks
nihar has score marks

print there respected total mark
"""

for name, info in details.items():
    total = 0
    for i in info["marks"]:
        total = total + i
    print(f"{name} has score total marks {total}")
