# Conway's Game of Life
import random
import time
import copy
WIDTH = 60
HEIGHT = 20

# Create a list of lists for the cells:
nextCell = []
for x in range(WIDTH):
    column = []  # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#")  # Add a lining cell
        else:
            column.append(" ")  # Add a dead cell
    nextCells.append(column)  # nextCells is a list of column lists

while True:  # Main program loop
    print("n\n\n\n\n")  # Separate each step with newlines
    currentCells = copy.deepcopy(nextCells)
# Print currentCells on the screen:
for y in range(HEIGHT):
    for x in range(WIDTH):
        print(currrentCells[x][y], end=" ")  # Print the # or space
    print()  # Print a newline at the end of the row

# Calculate the next step's cell based on current step's cells:
for x in range(WIDTH):
    for y in range(HIGHT):
        # Get neighboring coordinates:
