"""
Scoping in Functions
ek variable ki kaha tak range hoti hai

"""


def info():
    num1 = 100
    num2 = 200
    total = num1 + num2
    print(total)


def greet():
    name = "lakshay"
    print(f"Your name is {name}")


print("start")
info()
greet()
print("end")
# print(total)  # this will give error, local variable access nhi hoga
