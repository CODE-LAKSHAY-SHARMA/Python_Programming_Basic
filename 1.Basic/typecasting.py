# converting one data type to another data type
"""
int-> string
string ->int
float-> string
string ->float
int->float
float->int
"""
# concatenation
a = "300"
b = "200"
print(a + b)
# convert string to int
print(int(a) + int(b))
print(type(a))  # still the datatype remaining string

a = float(100)
print(a)


a = int(542.67)  # Nearest to zero
print(a)

a = int(-2.67)  # -2 will be output
print(a)


a = int("100")
print(a)


a = int("100.9")  # this will not be converted to integer, par float m ho jaayega
print(a)
