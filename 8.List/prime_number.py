"""
Print all prime number in list given
"""


# EASY WAY
def isprime(num: int) -> bool:
    factor = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factor += 1
    if factor == 2:
        return True
    return False


my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]
n = len(my_list)
for index in range(0, n):
    if isprime(my_list[index]) == True:
        print(my_list[index], end=" ")

print()
#  HARD WAY
my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]
for num in my_list:
    factor = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factor += 1
    if factor == 2:
        print(num, end=" ")


# BEST APPROACH ( excluding 1 and numberitself)
"""
Rather calculating the factor of num and then checking whether factor==2, We c
can assume that 1 and number Itself are divisible by nums and if i got 
the 3rd number also divisible by nums then it is not a prime number
"""


def is_primeNumber(num: int) -> bool:

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]

for num in my_list:
    if is_primeNumber(num):
        print(num, end=" ")
