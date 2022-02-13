suppliers = ["pens", "staplers", "flamethrowers", "binders"]
for i in range(len(suppliers)):
    print("Index " + str(i) + " in supplies is: " + suppliers[i])


# the same using enumerate function, this function returns two values:
# the index of the item in the list, and the item in the list itself

suppliers = ["pens", "staplers", "flamethrowers", "binders"]
for index, item in enumerate(suppliers):
    print("Index " + str(index) + " in supplies is: " + item)
