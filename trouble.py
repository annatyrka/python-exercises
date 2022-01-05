x = [1, 2, 2, 1, 5, 2, 1]
print(x)


def trouble(x, t):
    i = 0
    while i < len(x) - 1:
        if x[i] + x[i+1] == t:
            del x[i+1]
        else:
            i += 1
    return x


print(trouble(x, 3))
