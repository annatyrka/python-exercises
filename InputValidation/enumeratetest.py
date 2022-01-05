import pyinputplus as pyip


def adds_up_to_ten(numbers):
    numbers_list = list(numbers)
    for i, digit in enumerate(numbers_list):
        numbers_list[i] = int(digit)
    if sum(numbers_list) != 10:
        raise Exception('The digits must add up to 10, not %s.' %
                        (sum(numbers_list)))
    return int(numbers)


# adds_up_to_ten('45')
response = pyip.inputCustom(adds_up_to_ten)
