"""
Class object methods 
"""


class Student:
    # class variable/attributes
    idd = 0
    name = ""
    age = 0
    gender = ""

    # methods /class methods
    def display(self):
        print(self)
        print(f" ID = {self.idd}")
        print(f" Name = {self.name}")
        print(f" Age = {self.age}")
        print(f" Gender = {self.gender}")


s1 = Student()
s2 = Student()
# print(s1.id)  # for accessing the id from student class using (.dot)
s1.name = "lakshay"
s1.idd = 101
s1.age = 23
s1.gender = "Male"
# print(s1)
s1.display()  # reduces the line of code to print each class variable

s2.display()
