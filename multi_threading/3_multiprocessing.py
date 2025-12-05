"""Multiprocessing example showing parallel execution with separate processes.

This module demonstrates how to use multiprocessing.Process() to create
and run multiple processes that execute in parallel. Key concepts:
  - Process vs Thread: processes have separate memory spaces (true parallelism)
  - Process creation with target function and arguments
  - Process lifecycle: start() and join()
  - GIL-free execution across multiple CPU cores

Unlike threading which shares memory, each process has its own Python interpreter
and memory space, making multiprocessing ideal for CPU-bound tasks.

Run with: python3 3_multiprocessing.py
"""

import multiprocessing
import time
import logging

# Configure logging for process-safe output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(processName)-15s] %(message)s",
    datefmt="%H:%M:%S",
)


def worker_task(process_name: str, delay: int, iterations: int) -> None:
    """Execute a worker task that logs timestamps at regular intervals.

    This function runs in a separate process with its own memory space.
    Each process is independent and can run on a different CPU core.

    Args:
        process_name: Name of the process (used in logging)
        delay: Seconds to wait between iterations
        iterations: Number of times to log the timestamp
    """
    logging.info(f"Starting worker task with {iterations} iterations")

    for remaining in range(iterations, 0, -1):
        time.sleep(delay)
        logging.info(
            f"{process_name}: Timestamp={time.ctime()}, iterations_left={remaining}"
        )

    logging.info("Worker task complete")


def main() -> None:
    """Create and execute multiple processes in parallel."""
    logging.info("=== Multiprocessing example starting ===")
    logging.info(
        "Key difference from threading: each process has separate memory space"
    )

    # Create multiple processes with target function and arguments
    # Each process will run worker_task() independently
    processes = [
        multiprocessing.Process(
            target=worker_task, args=("Process-1", 1, 5), name="Worker-1"
        ),
        multiprocessing.Process(
            target=worker_task, args=("Process-2", 2, 5), name="Worker-2"
        ),
    ]

    # Start all processes (they execute in parallel on separate CPU cores if available)
    for process in processes:
        logging.info(f"Starting {process.name}")
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
        logging.info(f"{process.name} finished")

    logging.info("=== All processes finished ===")


if __name__ == "__main__":
    # Note: multiprocessing requires 'if __name__ == "__main__"' guard
    # on Windows and macOS to prevent spawning new processes recursively
    main()
