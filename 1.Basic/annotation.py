name = "lakshay"
print(name)

# changing varibale type
name = 123
print(name)

# mujhe ab name ke ander string hi fix karna hai integer m change nhi karna hai

name: str = "lakshay sharma"
print(name)
# ab m change karne ki koshish karu toh error aayega

name = 55  # this will give error but still print the output name as 55 , yeh sirf hmare samjhne k leye hai
print(name)


# example
name: str = "lakshay"
age: int = 100
gender: str = "Male"
adult: bool = True
percent: float = 99.98


adult = "xyz"  # this will give warning

# eska matlb ki num m list ke ander integer and string value dono ko store karwa sakte hai
nums: list[int | str]


# code with both number as well as string
AccountNumber: str | int = "aG56Gjhks"
print(AccountNumber)
print(type(AccountNumber))

"""
 this work because account number ko string and interger dono assign kara hai
 starting m eslye esme annotation wala error nhi aa rha hai
"""
AccountNumber = 9998
print(AccountNumber)
