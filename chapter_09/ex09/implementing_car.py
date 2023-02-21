from car import Car, ElectricCar

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()

used_car = Car('subaru', 'outback', 2019)
print(used_car.get_descriptive_name())

used_car.update_odometer(23_500)
used_car.read_odometer()

used_car.increment_odometer(100)
used_car.read_odometer()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()