from __future__ import print_function
tableData = [["apples", "oranges", "cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose", "goose"]]

for i in range(len(tableData)):
    for j in range(len(tableData[i])):
        print(tableData[i][j], end=' ')
    print("")
