def odd_or_even(arr):
    if arr == []:
        arr == [0]

    return ("even" if sum(arr) % 2 == 0 else "odd")


a = [1, 2, 3]
print(odd_or_even(a))
