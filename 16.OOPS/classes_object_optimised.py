"""
Class object methods , 
class variable assigning using setDetails method
and display the class method we make methods
"""


class Student:
    # class variable/attributes
    idd = 0
    name = ""
    age = 0
    gender = ""

    # methods /class methods
    def setDetails(self):
        self.idd = int(input("Enter Id "))
        self.name = input("Enter Name ")
        self.age = int(input("Enter Age "))
        self.gender = input("Enter Gender  ")

    def display(self):
        print(self)
        print(f" ID = {self.idd}")
        print(f" Name = {self.name}")
        print(f" Age = {self.age}")
        print(f" Gender = {self.gender}")


s1 = Student()
s1.setDetails()
s1.display()

s2 = Student()
s2.setDetails()
s2.display()
