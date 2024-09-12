# my_list = [5, 4, 3, 2, 7, 2, 8, 9, 7, 4]
# print(my_list)
# print(id(my_list))


# my_list.sort()  # In place sorting
# print(my_list)
# print(id(my_list))  # address will not changes


# print(sorted(my_list))
# print(my_list)

my_list = [5, 4, 3, 2, 7, 2, 8, 9, 7, 4]
# sort all number and then join them
# # phele ander hi ander sort kar deyne
# my_list.sort()

print(" ".join(str(num) for num in sorted(my_list)))
# main my_list m changes nhi hue hai
print(my_list)
