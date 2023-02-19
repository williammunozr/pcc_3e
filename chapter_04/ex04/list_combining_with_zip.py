names = ['alice', 'bob', 'charlie']
ages = [25, 30, 35]
for i in range(len(names)):
    print(names[i], ages[i])

# combining with zip
for name, age in zip(names, ages):
    print(name, age)