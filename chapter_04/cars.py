cars = ['mazda', 'bmw', 'audi', 'porsche', 'toyota']
print(cars)

for index, item in enumerate(cars):
    print(index, item)

print("")

for index, item in enumerate(cars, start=0):
    print(index, item)

print("")

for index in range(0, len(cars)):
    print(index, cars[index])