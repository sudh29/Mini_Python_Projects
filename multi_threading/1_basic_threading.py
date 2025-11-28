"""Import necessary modules"""

import threading
import time

# Print a message to indicate the start of threading
print("Threading")


# Define a custom thread class
class MyThread(threading.Thread):
    """
    Custom thread class that inherits from threading.Thread.
    Each thread instance takes a thread ID, name, and counter as arguments.
    """

    def __init__(self, thread_id, name, counter):
        """
        Initialize the thread with ID, name, and counter.
        """
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        """
        Run the thread and print its name, current time, and counter every second.
        """
        print(f"Start {self.name}\n")
        print_time(self.name, self.counter, 5)
        print(f"End {self.name}\n")


def print_time(thread_name, delay, counter):
    """
    Print the thread name, current time, and counter every 'delay' seconds.
    The function runs as long as 'counter' is greater than zero.
    """
    while counter:
        time.sleep(delay)
        print(thread_name, time.ctime(time.time()), counter)
        print()
        counter -= 1


# Create two threads
t1 = MyThread(1, "Thread-1", 1)
t2 = MyThread(2, "Thread-2", 2)

# Start the threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

# Print a message to indicate the end of the main program
print("Done")
