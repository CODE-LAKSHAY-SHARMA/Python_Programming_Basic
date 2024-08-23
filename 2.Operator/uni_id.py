# Unique ID
# this is not memory address
a = 5
print(id(a))

b = 10
print(id(b))


# now change is a
a += 3
print(id(a))  # the unqiue id changes
