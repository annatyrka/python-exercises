def diffArray(arr1, arr2):
    newArr = []

    for item in arr1:
        if item not in arr2:
            newArr.append(item)

    for item in arr2:
        if item not in arr1:
            newArr.append(item)
    return newArr


print(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]))
