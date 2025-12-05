"""Threading with locks to synchronize access to shared resources.

This module demonstrates how to use threading.Lock() to coordinate
multiple threads accessing a shared resource. Key concepts:
  - Lock acquisition with acquire() and release()
  - Context manager syntax (with statement) for cleaner lock usage
  - Critical section protection to prevent race conditions

Scenario: Three concurrent tasks (Payment, Mail, Page) print timestamps
while holding a lock to ensure output doesn't interleave.

Run with: python3 2_lock_threading.py
"""

import threading
import time
import logging

# Configure logging for thread-safe output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-15s] %(message)s",
    datefmt="%H:%M:%S",
)


# Create a global lock to synchronize access to shared resources
thread_lock = threading.Lock()


class WorkerThread(threading.Thread):
    """A thread that performs a task while synchronizing with a lock.

    This class demonstrates two approaches:
    1. Acquire lock, perform critical section, release lock
    2. Acquire lock before I/O, perform work outside critical section

    Parameters:
        thread_id: Unique identifier for the thread
        name: Display name (e.g., 'Payment', 'Sending Mail')
        iterations: Number of times to log the timestamp
        lock_before_work: If True, acquire lock before printing timestamps;
                         if False, acquire lock only for synchronization
    """

    def __init__(
        self, thread_id: int, name: str, iterations: int, lock_before_work: bool = True
    ) -> None:
        """Initialize the worker thread.

        Args:
            thread_id: Unique identifier for the thread
            name: Display name for logging
            iterations: Number of iterations to run
            lock_before_work: Whether to hold lock during work or just for synchronization
        """
        super().__init__(name=name)
        self.thread_id = thread_id
        self.iterations = iterations
        self.lock_before_work = lock_before_work

    def run(self) -> None:
        """Execute the worker thread with proper lock synchronization."""
        logging.info(f"Starting task (iterations={self.iterations})")

        if self.lock_before_work:
            # Approach 1: Hold lock during entire critical section
            with thread_lock:
                logging.info("Acquired lock - starting protected work")
                print_time(self.name, self.iterations, 5)
                logging.info("Releasing lock - work complete")
        else:
            # Approach 2: Brief lock for synchronization only
            with thread_lock:
                logging.info("Synchronized point reached")
            print_time(self.name, self.iterations, 5)

        logging.info("Task complete")


def print_time(task_name: str, delay: int, iterations: int) -> None:
    """Log task progress with timestamps at regular intervals.

    Args:
        task_name: Name of the task performing the work
        delay: Seconds to wait between iterations
        iterations: Number of times to log
    """
    for remaining in range(iterations, 0, -1):
        time.sleep(delay)
        logging.info(
            f"{task_name}: Timestamp={time.ctime()}, iterations_left={remaining}"
        )


def main() -> None:
    """Create and execute multiple worker threads with lock synchronization."""
    logging.info("=== Lock-based threading example starting ===")

    # Create threads with different behaviors:
    # t1: Holds lock during entire work (serialize access to print_time)
    # t2, t3: Acquire lock briefly for synchronization, then work independently
    threads = [
        WorkerThread(1, "Payment", iterations=1, lock_before_work=True),
        WorkerThread(2, "Sending Mail", iterations=5, lock_before_work=False),
        WorkerThread(3, "Loading Page", iterations=3, lock_before_work=False),
    ]

    # Start all threads (they execute concurrently)
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    logging.info("=== All tasks finished ===")


if __name__ == "__main__":
    main()
