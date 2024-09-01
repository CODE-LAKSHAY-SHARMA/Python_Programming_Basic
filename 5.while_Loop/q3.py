start_number = int(input("Enter a start number: "))

end_number = int(input("Enter an end number: "))
if end_number > start_number:
    while start_number <= end_number:
        print(start_number, end=" ")
        start_number = start_number + 1
else:
    print("please put end number greater than start numnber")
