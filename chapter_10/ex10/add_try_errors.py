print("Press 'q' to quit.")
while True:
    first_number = input('Enter the first number: ')
    if first_number == 'q':
        break

    # This is an opportunity for a function
    try:
        first_number = int(first_number)
    except ValueError:
        print(f"The value '{first_number}' is not a number.")
        continue

    second_number = input('Enter the second number: ')
    if second_number == 'q':
        break

    try:
        second_number = int(second_number)
    except ValueError:
        print(f"The value '{second_number}' is not a number.")
        continue

    print(f"The sum of {first_number} + {second_number} is {first_number + second_number}.")

