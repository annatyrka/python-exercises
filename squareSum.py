def square_sum(numbers):
    return sum(i**2 for i in numbers)


print(square_sum([1, 2, 3, 4]))


def monkey_count(n):
    return range(1, n+1)


print(monkey_count(9))


def remove_every_other(my_list):
    return my_list[::2]


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(x))
print(remove_every_other(x))
