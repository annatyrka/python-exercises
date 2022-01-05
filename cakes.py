def cakes(recipe, ingridients):
    number_of_cakes = []

    for keys in recipe:
        try:
            number_of_cakes.append(ingridients[keys] // recipe[keys])
        except KeyError:
            number_of_cakes.append(0)
    return min(number_of_cakes)

    # return (min(ingridients[keys] // recipe[keys] for keys in recipe if ingridients[keys]))


# must return 2
#print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
# must return 0
print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100,
             'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}))


def cakes2(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0
