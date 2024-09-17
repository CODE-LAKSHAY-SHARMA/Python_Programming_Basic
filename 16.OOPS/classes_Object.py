"""

"""


class Student:
    id = 0
    name = ""
    age = 0
    gender = ""


s1 = Student()
# print(s1.id)  # for accessing the id from student class using (.dot)
s1.name = "lakshay"
s1.id = 101
s1.age = 23
s1.gender = "Male"

print(id(s1))
print(s1.age)
print(s1.id)
print(s1.name)
print(s1.gender)

# creating the another object using same class Student
s2 = Student()
print(id(s2))
print(s2.age)
print(s2.id)
print(s2.name)
print(s2.gender)

# x=int()  # this is also the object rather than variable
# note in python everything is an Object
