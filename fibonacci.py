for row in range(1, 10):
    if row <= 5:
        for column in range(1, row+1):
            print("*", end=" ")
        print("")
    if row > 5:
        for column in range(row, 10):
            print("*", end=" ")
        print("")
