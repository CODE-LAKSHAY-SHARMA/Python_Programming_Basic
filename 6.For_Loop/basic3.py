"""
print 20 to  1
"""

for i in range(20, 0, -1):  # by default step size is +1 hoga , toh usko -1 karna padega
    print(i, end=" ")

# this will not work  because -1 is wrong here
for i in range(1, 20, -1):
    print(i)
