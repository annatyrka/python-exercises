import pyinputplus as pyip

bread = 0
protein = 0
cheese = 0
mayo = 0
mustard = 0
lettuce = 0
tomato = 0

prices_bread = {'wheat': 2, 'white': 1.5, 'sourdough': 3}
prices_proteins = {'chicken': 2, 'turkey': 4, 'ham': 3, 'tofu': 3.5}
prices_cheese = {'cheddar': 2, 'Swiss': 4, 'mozzarella': 2.5}
prices_sauces = {'mayo': 0.5, 'mustard': 1, }
prices_addons = {'lettuce': 2, 'tomato': 4}

bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'])
bread = int(prices_bread[bread_type])
protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
protein = int(prices_proteins[protein_type])
cheese = pyip.inputYesNo('Would you like some cheese? ')

if cheese == 'yes':
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
    cheese = int(prices_cheese[cheese_type])

mayo_yes = pyip.inputYesNo('Would you like some mayo? ')
if mayo_yes == 'yes':
    mayo = int(prices_sauces['mayo'])
mustard_yes = pyip.inputYesNo('Would you like some mustard? ')
mustard = int(prices_sauces['mustard'])
lettuce_yes = pyip.inputYesNo('Would you like some lettuce? ')
lettuce = int(prices_addons['lettuce'])
tomato_yes = pyip.inputYesNo('Would you like some tomato? ')
tomato = int(prices_addons['tomato'])
how_many = pyip.inputInt('How many sanwiches would you like? ', min=1)


total = (bread + protein + cheese + mayo + mustard + lettuce + tomato)*2
print(total)
