from pathlib import Path

contents = 'I love Golang programming.\n'
contents += 'I love creating CLI tools.\n'
contents += 'I also love working with Rest API.\n'

path = Path('golang_programming.txt')
path.write_text(contents)
