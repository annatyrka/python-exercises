list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
print(list(zip(list1, list2)))
list4 = list(i + j for i, j in zip(list1, list2))
print(list4)
