name = "william"

message = f"Hallo {name.title()}, would you like to learn some Python today?"
print(message)

full_name = "william munoz"
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

quote = "Your time is limited, so don't waste it living someone else's life."
print(f'Steve Jobs once said: "{quote}"')

famous_person = "Steve Jobs"
message = f'{famous_person} once said: "{quote}"'
print(message)

full_name = " william   munoz  "
name_array = full_name.split()
first_name = name_array[0].strip()
last_name = name_array[1].strip()
print(f"Firstname:\t{first_name.title()}\nLastname:\t{last_name.title()}")

filename = 'python_notes.txt'
print(filename.removesuffix(".txt"))