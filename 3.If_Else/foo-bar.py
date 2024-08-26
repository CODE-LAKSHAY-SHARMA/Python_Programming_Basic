"""
#Ask a number from user

if num  is divisble by 3  ->>  FOO
if num  is divisble by 5 ->   BAR
num is divisible by both 3 and 5 ->> FOOBAR
else ->  Invalid
"""

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FOOBAR")
elif num % 3 == 0:
    print("FOO")
elif num % 5 == 0:
    print("BAR")
else:
    print("Invalid")
