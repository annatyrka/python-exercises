items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


def get_item(item):
    return len(item[0])


def lenght(item):
    return len(e)


# python will pass each item to a function
items.sort(key=lambda item: item[1])
print(items)
