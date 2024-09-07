"""
Method in string
"""

a = "lakshay sharma"

print(a.isalpha())
print(a.isupper())
print(a.islower())

b = "12334"
print(b.isdigit())

print(a.upper())
print(a.lower())
print(a.title())  # make first letter of word capital

print(a.index("h"))  # agar value exist ni karti toh error deyga output par

print(
    a.find("h")
)  # agar value exist nhi karti , es case m error nhi deyga (-1) print karwa deyga
print(a.find("zzz"))  # return -1 if does not exits
