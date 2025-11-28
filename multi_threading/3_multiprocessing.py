import multiprocessing
import time

# Print a message to indicate the start of multiprocessing
print("Multiprocessing")


def print_time(process_name, delay, counter):
    """
    Print the process name, current time, and counter every 'delay' seconds.
    The function runs as long as 'counter' is greater than zero.
    """
    while counter:
        time.sleep(delay)
        print(f"{process_name}: {time.ctime(time.time())}, Counter: {counter}")
        print()
        counter -= 1


# Create two processes
p1 = multiprocessing.Process(target=print_time, args=("Process-1", 1, 5))
p2 = multiprocessing.Process(target=print_time, args=("Process-2", 2, 5))

# Start the processes
p1.start()
p2.start()

# Wait for both processes to complete
p1.join()
p2.join()

# Print a message to indicate the end of the main program
print("Done")
