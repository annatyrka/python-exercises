import random
numStreaks = 0
record_list = []

for experiment_number in range(10000):
    for i in range(99):
        a = random.randint(0, 1)
        if a == 0:
            record_list.append("T")
        else:
            record_list.append("H")

    for j in range(93):
        if record_list[j:j+6] == ["H", "H", "H", "H", "H", "H"] or record_list[j:j+6] == ["T", "T", "T", "T", "T", "T"]:
            numStreaks += 1


print(numStreaks)
