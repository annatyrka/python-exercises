def switch_ligths(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)


market_2nd = {'ns': 'green', 'ew': 'red'}


switch_ligths(market_2nd)
print(market_2nd)
