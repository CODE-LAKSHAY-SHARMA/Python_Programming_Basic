name = "lakshay"
age = 23
gender = "male"

# 1st way to print the variable
print("my name is", name)  # , laangne ke baad extra space deyta hai

# 2nd way
print("my name is", name, "and age is ", age, "and gender is ", gender)

# 3rd way format string
print(f"my name is {name}")
print(f"my age is {age}")
print(f"my gender is {gender}")

# 4th way string identifier
"""
%s-> String
%d -> integer
%f  -> float
"""

print("my name is %s" % name)
print("my age is %d" % age)
print("my gender is %s" % gender)
print("my name is %s and age is %d and gender is %s " % (name, age, gender))


# 5th method  ( direct methods)  f-string debugging in Python.

print(f"{name =}")
print(f"{age =}")
print(f"{gender =}")
