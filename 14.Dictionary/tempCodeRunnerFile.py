list1 = [4, 5, 6, 4, 4, 3, 2, 3, 3, 1, 4, 8, 9, 9, 10]
result = {}
for i in list1:
    result[i]=result.get(i,0)+1
    
print(result)