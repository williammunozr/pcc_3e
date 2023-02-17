pizzas = ['ortolana', 'rustica', 'alla pala', 'pesto genovese', 'fugazzeta', 'e fichi',
          'grandma pie', 'apizza', 'fiori di zucca', 'pugliese', 'prosciutto e funghi',
          'detroit-style', 'garlic fingers', 'tomato pie', 'fugazza', 'al padellino',
          'grilled', 'carbonara', 'pinsa romana', 'vegariana', 'stuffed', 'fritta',
          'chicago thin crust', 'california-style', 'tarte flambée', 'prosciutto',
          'quattro stagioni', 'ai frutti di mare', 'greek-style', 'manakish', 'alla diavola',
          'romana', 'primavera', 'stromboli', 'al taglio', 'pizzette', 'bianca', 'ai funghi',
          'hawaiian', 'chicago-style deep dish', 'sicilian', 'capricciosa', 'quatro formaggi',
          'new york-style', 'marinara', 'caprese', 'pepperoni', 'calzone', 'margherita',
          'napoletana']

# create a for loop that prints the pizzas
for pizza in pizzas:
    print(pizza)

print("")

# sort the pizzas list without change the original
ordered_pizzas = sorted(pizzas)
for pizza in ordered_pizzas:
    print(pizza)

print("")

# sort the original pizzas list
pizzas.sort()
for pizza in pizzas:
    print(pizza)

print("")

# sort the pizzas list in reverse without change the original
reversed_pizzas = sorted(pizzas, reverse=True)
for pizza in reversed_pizzas:
    print(pizza)

print("")

# create a message with every pizza and assign a number to each item
for index, pizza in enumerate(pizzas, start=1):
    print(f"{index}. I like {pizza}")