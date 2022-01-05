def separate_types(seq):
    a, b, c = [], [], []
    output = {int: a, str: b, bool: c}

    for item in seq:
        if isinstance(item, int):
            output[int].append(item)
        if isinstance(item, str):
            output[str].append(item)
        if isinstance(item, bool):
            output[bool].append(item)
    if not a:
        output.pop(int)
    if not b:
        output.pop(str)
    if not c:
        output.pop(bool)
    return output


a = ['a', 1, 2, 'b']

print(separate_types(a))
