"""
Scoping in Functions
ek variable ki kaha tak range hoti hai

"""


def info():
    num1 = 100
    num2 = 200
    total = num1 + num2
    print(total)
    greet()


def greet():
    name = "lakshay"
    print(f"Your name is {name}")
    info()


print("start")
info()
greet()
print("end")
