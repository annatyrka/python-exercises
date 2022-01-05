def max_sequence(arr):
    max_value = 0
    for i in range(len(arr)):
        for j in range(len(arr)+1):
            if sum(arr[i:j]) > max_value:
                max_value = sum(arr[i:j])
    return max_value


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# should be 6: [4, -1, 2, 1]

print(max_sequence([5, 2, 1]))
