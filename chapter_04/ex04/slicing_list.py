players = ['charles', 'martina', 'michael', 'florence', 'eli']

# prints a slice of the list
print(players[0:3]) # prints ['charles', 'martina', 'michael']

print(players[1:4])

print(players[:2])

print(players[2:])

print(players[-3:]) # last three elements of the list

print(players[:])

print("")

# copying a list
bkp_players = players[:]
print(bkp_players)

# Loop in a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())