from typing import List


class Student:
    def __init__(self, roll_no: int, name: str, age: int, gender: str, marks=[]):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks

    def total(self) -> int:
        # return sum(self.marks)
        t = 0
        for n in self.marks:
            t = t + n
        return t

    def display(self):
        print(f" RollNo = {self.roll_no}")
        print(f" Name = {self.name}")
        print(f" Age = {self.age}")
        print(f" Gender = {self.gender}")
        print(f" marks = {self.marks}")


# s1 = Student(1, "lakshay", 23, "Male", [56, 7, 8, 98, 23, 12])
# s2 = Student(2, "barkha", 23, "Female", [70, 67, 88, 23, 11])
# OTHER WAY OF ABOVE

# # concept of List _Of_Object
# # students_data = [s1, s1]
# students_data = [
#     Student(1, "lakshay", 23, "Male", [56, 7, 8, 98, 23, 12]),
#     Student(2, "naveen", 27, "Female", [70, 67, 88, 23, 11]),
# ]
# students_data[1].display()
# print(students_data[0].marks)
# print(students_data[0].name)
# print(students_data[1].total())


# # print the age of naveen as 27 output
# print(students_data[1].age)


# creating menu


student_details: List[Student] = []  # student name ka Object X aa gaya hai uper

while True:
    print("1) Add a student ")
    print("2) Remove a student ")
    print("3) Display  all student details")
    print("4) Update Student details ")
    print("5) Display only one student details ")
    print("6) Exits ")
    choice = int(input("Enter your Choice from 1 to 5=> "))
    if choice == 1:
        roll_no = int(input("Enter roll no "))
        name = input("Enter name ")
        age = int(input("Enter age "))
        gender = input("Enter gender ")
        no_of_subject = int(input("enter number of subject"))
        # entering the marks of the student
        marks1 = []
        for i in range(no_of_subject):
            m = int(input("enter marks of Subject {i}"))
            marks1.append(m)
        x = Student(roll_no, name, age, gender)
        student_details.append(x)
        print(student_details)

    elif choice == 2:
        pass
    elif choice == 3:
        if len(student_details) == 0:
            print("No student Found!! ")
        else:
            for i in student_details:  # object iterate karegea
                i.display()
    elif choice == 4:
        pass
    elif choice == 5:
        rno = int(input("Enter use roll no you want to search for ?  "))
        for stu in student_details:
            if stu.roll_no == rno:  # object in list of student_details
                stu.display()
                break
        else:
            print("No roll number found ! ")

    elif choice == 6:
        break
    elif choice == 7:
        break
    else:
        print("Invalid choice")
