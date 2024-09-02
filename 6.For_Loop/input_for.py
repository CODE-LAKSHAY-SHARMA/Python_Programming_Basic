# ask start and end

start = int(input("enter start=="))
end = int(input("enter end=="))

if start < end:
    for i in range(start, end + 1):
        print(i, end=" ")
else:
    for i in range(start, end - 1, -1):
        print(i, end=" ")
