class Student:

    # magic/dunder method
    # def __init__(self):
    #     # intialisor hain!!! constructor nhi hai yeh( memory allocate nhi hoti)
    #     # print(self)  # s1 ka address aayega
    #     # print("this is an init methods")
    #     self.idd = int(input("Enter Id "))
    #     self.name = input("Enter Name ")
    #     self.age = int(input("Enter Age "))
    #     self.gender = input("Enter Gender  ")
    #     self.address = input("Enter address  ")
    #     # self.display()

    def __init__(self, idd: int, name: str, age: int, gender: str, address: str = ""):
        self.idd = idd
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def updateName(self, new_name) -> None:
        self.name = new_name

    def display(self):
        # print(self)
        print(f" ID = {self.idd}")
        print(f" Name = {self.name}")
        print(f" Age = {self.age}")
        print(f" Gender = {self.gender}")
        print(f" address = {self.address}")


# s1 = Student(101, "lakshay", 23, "Male")
s1 = Student(idd=101, address="dehradun", gender="male", name="lakshay", age=23)
s1.display()
# s1.updateName("abhishek")
# s1.display()

# agar m setDetails karna bhul jaate hai toh ->  magic/dunder method use karte hai
