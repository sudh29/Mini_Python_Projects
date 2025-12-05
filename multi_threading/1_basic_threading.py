"""Simple threading example demonstrating concurrent task execution.

This module shows how to create and run multiple threads that execute
independently. Key concepts covered:
  - Custom thread class inheriting from threading.Thread
  - Thread lifecycle: start() and join()
  - Concurrent execution with coordinated timing

Run with: python3 1_basic_threading.py
"""

import threading
import time
import logging

# Configure logging for clearer thread output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12s] %(message)s",
    datefmt="%H:%M:%S",
)


# Define a custom thread class
class MyThread(threading.Thread):
    """
    Custom thread class that inherits from threading.Thread.
    Each thread instance takes a thread ID, name, and counter as arguments.
    """

    def __init__(self, thread_id: int, name: str, counter: int) -> None:
        """Initialize the thread with ID, name, and counter.

        Args:
            thread_id: Unique identifier for the thread
            name: Display name for the thread (used in logging)
            counter: Number of iterations to run
        """
        super().__init__(name=name)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self) -> None:
        """Execute the thread: log start, run iterations, then log end."""
        logging.info(f"Starting thread execution (iterations={self.counter})")
        print_time(self.name, self.counter, 5)
        logging.info("Thread execution complete")


def print_time(thread_name: str, delay: int, counter: int) -> None:
    """Log the thread name and current time every 'delay' seconds.

    Args:
        thread_name: Name of the thread (used in logging)
        delay: Seconds to wait between iterations
        counter: Number of iterations to run
    """
    while counter:
        time.sleep(delay)
        logging.info(f"{thread_name}: {time.ctime()} (iterations_left={counter})")
        counter -= 1


def main() -> None:
    """Create, start, and join two worker threads."""
    logging.info("=== Threading example starting ===")

    # Create two threads with different iteration counts
    t1 = MyThread(1, "Thread-1", 1)
    t2 = MyThread(2, "Thread-2", 2)

    # Start the threads (they execute concurrently)
    t1.start()
    t2.start()

    # Wait for both threads to complete before exiting main
    t1.join()
    t2.join()

    # Print a message to indicate the end of the main program
    logging.info("=== All threads finished ===")


if __name__ == "__main__":
    main()
