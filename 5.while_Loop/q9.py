# from 1 to 10 , count how many even number are there

start = 1
end = 100
count = 0
while start <= end:
    if start % 2 == 0:
        count += 1
    start += 1
print(count)
