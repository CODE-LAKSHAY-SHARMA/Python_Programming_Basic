"""
QUESTION

Given a list list1=[4,5,6,4,4,3,2,3,3,1,4,8,9,9,10], find the occurence of each 
element in the given list and store them in dictionary and print it

output
{
    4: 4
    5: 1
    6: 1
    3 : 3
    2 : 1
    1 : 1
    8 : 1
    9 : 2
    10:  1
}
"""

list1 = [4, 5, 6, 4, 4, 3, 2, 3, 3, 1, 4, 8, 9, 9, 10]
result = {}
for i in list1:
    if i in result:
        result[i] = result[i] + 1
    else:
        result[i] = 1
print(result)


# now to print the maximum frequency number
count = 0
max_count = 0
for i in result.values():
    if i > count:
        count = i
    else:
        max_count = count
print(max_count)  # 4 aayeaga , 4 number 4 baar repeat hua hai

# other approach
# list1 = [4, 5, 6, 4, 4, 3, 2, 3, 3, 1, 4, 8, 9, 9, 10]
# result = {}
# for i in list1:
#     result[i]=result.get(i,0)+1

# print(result)
