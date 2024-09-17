class Student:
    # methods /class methods
    def setDetails(self):
        self.idd = int(input("Enter Id "))
        self.name = input("Enter Name ")
        self.age = int(input("Enter Age "))
        self.gender = input("Enter Gender  ")
        self.address = input("Enter address  ")
        s1.display()

    def display(self):
        print(self)
        print(f" ID = {self.idd}")
        print(f" Name = {self.name}")
        print(f" Age = {self.age}")
        print(f" Gender = {self.gender}")
        print(f" address = {self.address}")


s1 = Student()
s1.setDetails()
# s1.display()
