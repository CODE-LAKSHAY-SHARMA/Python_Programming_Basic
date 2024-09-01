"""
Factor of the number , print all of them 
"""

# BASIC APPROACH BRUTE FORCE APPROACH
# def factor(x: int):
#     i = 1
#     while i <= x:
#         if x % i == 0:
#             print(i)
#         i = i + 1

# a = int(input("enter the number => "))
# print(factor(a))


# OPTIMIZE SOLUTION
# First divide the num by 2 and then find the factor for half of the num
# def factor2(x: int) -> None:
#     i = 1
#     while i <= x // 2:
#         if x % i == 0:
#             print(i)
#         i = i + 1
#     # print(x)


# a = int(input("enter the number => "))
# print(factor2(a))


# OPTIMIZE APPORACH 2 -> taking square of the num , and then divide it by number
# and in that we cannot move while loop i till root of number


def factor3(x: int) -> None:
    root = x * 0.5
    count = 1
    i = 1
    while i <= root + 1:
        if x % i == 0:
            count = x // i
            print(count)
        i = i + 1


a = int(input("enter the number => "))
print(factor3(a))
