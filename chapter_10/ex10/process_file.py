import sys


def find_record_by_surname(input_surname):
    found = False
    with open("books.txt", "r") as f:
        for line in f:
            surname = line.split(',')[0]
            if surname.upper() == input_surname.upper():
                found = True
    return found


def return_details_by_surname(input_surname):
    details = []
    with open("books.txt", "r") as f:
        for line in f:
            details = line.split(',')
            if details[0] == input_surname.title():
                break
    return details


def find_record_by_month_of_birth(input_month):
    if len(input_month) != 2:
        input_month = "0" + input_month
    found = False
    with open("books.txt", "r") as f:
        for line in f:
            month = line.split(',')[6].split('/')[1]
            if input_month == month:
                found = True
                break
    return found


def return_details_by_month_of_birth(input_month):
    if len(input_month) != 2:
        input_month = "0" + input_month
    details = ""
    with open("books.txt") as f:
        for line in f:
            if line.split(',')[6].split('/')[1] == input_month:
                details = details + line
    return details


if __name__ == "__main__":
    print("Menu Choices")
    print("============")
    print("1: Search contacts by surname")
    print("2: Search contacts by month of birth")
    print("3: Add a new contact to books.txt")
    print("4: Exit")

    choice = input("Enter your choice: ")
    while choice != "4":
        if choice == "1":
            input_surname = input("Enter a surname to search in books.txt file: ")
            if find_record_by_surname(input_surname):
                print(f"The record {input_surname} was found in the books.txt file.")
                print("The details for that contact are:")
                print(return_details_by_surname(input_surname))
            else:
                print(f"The record {input_surname} was not found in the books.txt file.")
        if choice == "2":
            input_month = input("Enter the month of birth (1-12) to search in books.txt file: ")
            if find_record_by_month_of_birth(input_month):
                print("The details for the contact(s) with the entered month of birth are: ")
                print(return_details_by_month_of_birth(input_month))
            else:
                print(f"No record with {input_month} of birth was found in books.txt file.")

        choice = input("Enter your choice: ")

    print("Goodbye!")
    sys.exit(0)
