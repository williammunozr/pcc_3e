bycicles = ["trek", "cannondale", "redline", "specialized"]
print(bycicles)

# accesing the first element of the list
print(bycicles[0].title())

# special syntax for accessing the last element in a list
print(bycicles[-1].title())

# people
people = ["axl", "angus", "slash", "brian", "grohl", "steven"]
for i in range(0, len(people)):
    print(people[i])

for i in range(0, len(people)):
    print(f"Hallo {people[i].title()}")

# modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
for i in range(0, len(motorcycles)):
    print(f"motorcycle {i}: {motorcycles[i].title()}")

# adding elements to a list
motorcycles.append('honda')
print(f"motorcyles: {motorcycles}")

# initialize an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(f"motorcyles: {motorcycles}")

# inserting elements into a list
motorcycles.insert(0, 'ducati')
print(f"motorcyles: {motorcycles}")

# remove elements from a list

# remove an item using the del statement
del motorcycles[0]
print(f"motorcyles: {motorcycles}")

# remove an item using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"motorcyles: {motorcycles}")

# remove the last item from the list
popped_motorcycle = motorcycles.pop()
print(f"motorcyles: {motorcycles}")
print(f"popped motorcycle: {popped_motorcycle.title()}")

# popping item from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"motorcyles: {motorcycles}")
print(f"first owned motorcyle: {first_owned.title()}")

# removing an item by value
# this is useful when you don't know the position of the item
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(f"motorcyles: {motorcycles}")