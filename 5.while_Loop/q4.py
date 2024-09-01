# write a program to print the number from start number and end number
# and if the start number is greater than end number than print from end number to start number

start_number = int(input("Enter a start number: "))
end_number = int(input("Enter an end number: "))
i = start_number
j = end_number

if j > i:
    while i <= j:
        print(i, end=" ")
        i = i + 1
else:
    while j <= i:
        print(j, end=" ")
        j = j + 1
