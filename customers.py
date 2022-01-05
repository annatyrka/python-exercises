
def add_length(str_):

    lst = str_.split()
    lst2 = []
    for i in range(len(lst)):
        lst[i] = lst[i] + " " + str(len(lst[i]))
    return lst


def add_length2(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]


print(add_length('you will win '))
