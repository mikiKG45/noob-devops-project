import time

start_time = time.time()

while True:
    elapsed_seconds = int(time.time() - start_time)
    print(f"Now it passed {elapsed_seconds} seconds")
    time.sleep(1)
    if elapsed_seconds >= 10:
        break