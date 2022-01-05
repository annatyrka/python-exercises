def duck_duck_goose(players, goose):
    try:
        return players[goose-1]
    except IndexError:
        return players[goose % len(players) - 1]


print(duck_duck_goose(["a", "b", "c", "d"], 40))
