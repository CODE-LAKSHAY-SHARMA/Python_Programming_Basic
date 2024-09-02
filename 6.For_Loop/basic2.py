"""
Print  1 to 20 

output : 2 4 6 8 10 12---20
"""

# APPROACH 1 : basic
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Approach 2:  STEP CONCEPT

for i in range(2, 21, 2):
    print(i, end=" ")
