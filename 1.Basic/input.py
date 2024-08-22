# input function ke ander kuch bhi likho it will take it as a string ,
# eslye humko datatype input se phele bta hota hai


a = int(input("enter value of a "))
b = int(input("enter value of b "))

total = a + b
print(f"your total is equal to {total}")


# take 3 input and print the average

num1 = int(input("Enter value 1 "))
num2 = int(input("Enter value 2 "))
num3 = int(input("Enter value 3 "))


average = (num1 + num2 + num3) / 3
# print(f"the average of 5 numbner is {average}")
# the answer is cominng is 34.566666666665  but we need till upto 2 decimals
print(f"the average of 5 number is {average:.2f}")
