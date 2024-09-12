"""
my string : Count Alphabets, digits ,  spaces and symbols
"""


def count_my_string(my_string: str) -> None:
    alphabets = 0
    digits = 0
    space = 0
    symbols = 0

    for ch in my_string:
        if "a" <= ch <= "z":
            alphabets = alphabets + 1
        elif "A" <= ch <= "Z":
            alphabets = alphabets + 1
        elif "0" <= ch <= "9":
            digits = digits + 1
        elif ord(ch) == 32:
            space = space + 1
        else:
            symbols = symbols + 1
    print(f"total number of Alphabets are {alphabets}")
    print(f"total number of digits are {digits}")
    print(f"total number of space are {space}")
    print(f"total number of symbols are {symbols}")


my_string = "dasd54243ASDFJASD*(@#$  JJSN423/-+/+*asd)"
print(count_my_string(my_string))
