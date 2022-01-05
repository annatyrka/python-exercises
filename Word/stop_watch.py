import time

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.\n Press Ctrl-C to quit.')
input()
print("Started.")
start_time = time.time()
last_time = start_time
lap_num = 1

# Start tracking the lap times.

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f"Lap {lap_num}: total time: {total_time}, lap time: {lap_time}")
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone')
