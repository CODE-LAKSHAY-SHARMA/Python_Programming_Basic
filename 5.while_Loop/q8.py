# start to end number , print total of all even number

start = 1
end = 100
sum = 0

while start <= end:
    if start % 2 == 0:
        sum = sum + start
        start = start + 1
    else:
        start += 1
print(sum)
