"""
1. start to end : total all the number(1+2+3---38+--n)
2. start to end :  total all the number divisible by 7
"""

start = int(input("enter start=="))
end = int(input("enter end=="))

# total = 0
# for i in range(start, end + 1):
#     total = total + i
# print(total)

# 2 part of question
total = 0
for i in range(start, end + 1):
    if i % 7 == 0:
        total = total + i
print(total)
