"""Asyncio example demonstrating concurrent task execution with async/await.

This module shows how to use Python's asyncio library to run multiple
coroutines concurrently. Key concepts covered:
  - Coroutines and async/await syntax
  - Event loop for managing concurrent execution
  - asyncio.gather() for running tasks concurrently
  - Async I/O operations without threads

Unlike threading, asyncio runs on a single thread using an event loop.
It's ideal for I/O-bound operations like network requests and file operations.

Run with: python3 4_asyncio.py
"""

import asyncio
import time
import logging

# Configure logging for clearer asyncio output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)-15s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("asyncio_demo")


async def worker_task(
    task_id: int, task_name: str, delay: float, iterations: int
) -> None:
    """Execute an async worker task that logs timestamps at regular intervals.

    This coroutine runs concurrently with other coroutines in the event loop.
    The await asyncio.sleep() call yields control to allow other tasks to run.

    Args:
        task_id: Unique identifier for the task
        task_name: Display name for the task (used in logging)
        delay: Seconds to wait between iterations (uses asyncio.sleep)
        iterations: Number of times to log the timestamp
    """
    logger.info(f"Task {task_id} ({task_name}) starting with {iterations} iterations")

    for remaining in range(iterations, 0, -1):
        await asyncio.sleep(delay)  # Yields control to event loop
        logger.info(
            f"Task {task_id} ({task_name}): {time.ctime()}, iterations_left={remaining}"
        )

    logger.info(f"Task {task_id} ({task_name}) complete")


async def main() -> None:
    """Create and run multiple coroutines concurrently using asyncio."""
    logger.info("=== Asyncio example starting ===")
    logger.info(
        "Key benefit: runs concurrently on single thread without GIL limitations"
    )

    # Create multiple coroutines (not yet executing)
    tasks = [
        worker_task(1, "Task-A", delay=1.0, iterations=5),
        worker_task(2, "Task-B", delay=2.0, iterations=5),
        worker_task(3, "Task-C", delay=1.5, iterations=4),
    ]

    # Run all coroutines concurrently using gather()
    # gather() waits for all tasks to complete and returns their results
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()

    logger.info(
        f"=== All tasks finished (total time: {end_time - start_time:.2f}s) ==="
    )
    logger.info("Note: Tasks ran concurrently, so total time < sum of all delays")


if __name__ == "__main__":
    # Run the async main() function in the event loop
    asyncio.run(main())
