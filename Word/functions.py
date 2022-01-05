def multiply_by_nine_fifth(number):
    return number * (9/5)


def getFahrenheit(celsius):
    return multiply_by_nine_fifth(celsius) + 32


# print(getFahrenheit(15))


list1 = [1, 2, 3, 4]
# list1.pop(0)
# print(list1)


def change_list(lst):
    lst.append('flower')


change_list(list1)
print(list1)

for i in range(10, 1, -1):
    print(i)

for item in list1:
    print(item)

for i in range(len(list1)):
    print(list1[i])
