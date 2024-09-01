"""
Keep asking the input from the user untill it get 0 
and print/calculate the total
"""

total = 0
while True:
    num = int(input("Enter number:-> "))
    if num == 0:
        break
    total = total + num
print(total)
