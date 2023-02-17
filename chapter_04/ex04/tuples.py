# a tuple is a list that its values cannot be changed
dimensions = (200, 50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

# loop over all the values in a tuple using a for loop
for index, item in enumerate(dimensions):
    print(f"{index}. {item}")

print("")

# loop over all the values in a tuple using a for loop - without enumerate
for dimension in dimensions:
    print(dimension)

print("")

# changing a tuple redefining it
dimensions = (400, 100)
print("Modified dimensions:\n")
for dimension in dimensions:
    print(dimension)
