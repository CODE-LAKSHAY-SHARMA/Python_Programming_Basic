# To check the data type of the variable
a = 56

if type(a) == int:
    print("Integer value hain!!")
else:
    print("Integer value nhi hai")
# another way to check the data type by using isinstance of
b = 58
if isinstance(b, int):
    print("YES")
else:
    print("NO")


a = -10
b = -56
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")
