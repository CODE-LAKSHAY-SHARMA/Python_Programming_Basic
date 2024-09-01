"""
control statement : 

1 . continue :  skip the below part of the code and move to next part of the loop
2. break: completly break the loop
"""

# i = 1
# while i <= 5:
#     print("hello")
#     i = i + 1
#     if i == 2:
#         continue
#     print("good")
#     print("bye")
#     print("done")


# i = 1
# while i <= 5:
#     print("hello")
#     if i == 3:
#         continue  # i==3 hoti hi i update nhi hoga wahi 3 par repeat print hoga infinity time
#     i = i + 1


i = 1
while i <= 5:
    print("hello")
    if i == 3:
        break  # loop break hoga 3 par hi
    i = i + 1
