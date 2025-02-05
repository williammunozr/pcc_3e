favorites_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'will': 'golang',
}

# sort the keys as they're returned in the for loop
for name in sorted(favorites_languages.keys()):
    print(f"{name.title()}, thank you for taking the pool.")

print("")

# looping through all the values in a dictionary
for language in sorted(favorites_languages.values()):
    print(f"{language.title()}")

print("")

# sort a dict in place
favorites_languages = dict(sorted(favorites_languages.items()))
for person, language in favorites_languages.items():
    print(f"Person: {person.title()}, Language: {language.title()}")
