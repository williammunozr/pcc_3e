height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("You are tall enough to ride!")
else:
    print("You will be able to ride when you are a little older.")

# modulo
number = input("Enter a number, and I will tell you if it is even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")