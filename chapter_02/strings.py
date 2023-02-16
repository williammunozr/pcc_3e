name = "William Munoz"

print(name.upper())
print(name.lower())

name_arr = name.split() # space is the default separator

first_name = name_arr[0]
last_name = name_arr[1]

print(first_name.lower())
print(last_name.lower())

full_name = f"{first_name} {last_name}"
print(full_name.lower())

print(f"Hallo, {full_name.title()}!")

# Remove white spaces at the beginning
cool_language = " python"
print(f"cool language: {cool_language.rstrip()}") # remove whitespaces from right
print(f"cool_language: {cool_language.lstrip()}") # remove whitespaces from left
print(f"cool language: {cool_language.strip()}") # remove whitespaces from left and right