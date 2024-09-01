"""
5674 to 10983 number , how many number are divisible by 7 ?
"""

start = 5674
end = 10983
count = 0
while start <= end:
    if start % 7 == 0:
        count += 1
    start += 1
print(f"total number divisible between {start} and {end} is -> {count}")


"""
5674 to 10983 number , how many number are divisible by 2 and 7 ?
"""

start = 5674
end = 10983
count = 0
while start <= end:
    if start % 7 == 0 and start % 2 == 0:
        count += 1
    start += 1

print(f"total number divisible between {start} and {end} is -> {count}")
