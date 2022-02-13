list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for item in list1:
    if item > 150:
        break
    if item % 5 == 0:
        print(item)
