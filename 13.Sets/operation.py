"""
Methods of SET
"""

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# set3=set1+set2  # we cannot do it
set3 = set1 - set2  # DIFFERENCE CAN BE CALCULATED
# set3=set1*set2 # we cannot do it
# set3=set1/set2  # we cannot do it
print(set3)

set4 = set2 - set1  # jo element set2 m hai par set 1 m nhi hone chaiye
print(set4)
