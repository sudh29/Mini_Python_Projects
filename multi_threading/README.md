# Multi-threading, Multi-processing, and Async I/O in Python

This directory contains practical examples demonstrating different approaches to concurrent programming in Python. Each module focuses on a specific concurrency model with real-world use cases and best practices.

## Overview of Concurrency Models

### Threading vs Multiprocessing vs Asyncio

| Aspect              | Threading                          | Multiprocessing             | Asyncio                             |
| ------------------- | ---------------------------------- | --------------------------- | ----------------------------------- |
| **Execution Model** | Multiple threads in single process | Multiple separate processes | Single thread with event loop       |
| **Memory**          | Shared memory space                | Separate memory per process | Shared memory (single thread)       |
| **GIL**             | Limited by Global Interpreter Lock | No GIL limitation           | No GIL needed (single thread)       |
| **Best For**        | I/O-bound tasks                    | CPU-bound tasks             | I/O-bound tasks (network, files)    |
| **Overhead**        | Low                                | High                        | Very low                            |
| **Synchronization** | Locks, semaphores, events          | Pipes, queues               | No synchronization needed (usually) |
| **Complexity**      | Medium                             | High                        | Medium                              |

---

## File Descriptions

### 1. `1_basic_threading.py` - Introduction to Threading

**Purpose:** Demonstrates the basics of creating and managing threads using the `threading` module.

**Key Concepts:**

- Creating custom thread classes by inheriting from `threading.Thread`
- Thread lifecycle: `start()` and `join()`
- Concurrent execution on a single process
- Thread naming and identification

**Use Case:** I/O-bound operations like network requests, file reading, or API calls.

**Example Scenario:**

```
Two threads execute concurrently, printing timestamps at different intervals.
While one thread waits, the other can execute, making efficient use of wait time.
```

**When to Use:**

- Web scraping with multiple simultaneous requests
- Handling multiple client connections in a server
- Responsive UI applications where I/O operations shouldn't block the UI

---

### 2. `2_lock_threading.py` - Thread Synchronization with Locks

**Purpose:** Demonstrates how to use locks to safely synchronize access to shared resources between threads.

**Key Concepts:**

- Lock objects for protecting critical sections
- `acquire()` and `release()` methods
- Context managers (`with` statement) for automatic lock management
- Race condition prevention
- Two synchronization strategies (lock during work vs. brief synchronization)

**Lock Objects (Mutexes):**

> Imagine a public restroom with a single lock on the door. Only one person can enter at a time, ensuring privacy and preventing conflicts.

**Use Case:** Preventing race conditions when multiple threads access shared data.

**Example Scenario:**

```
Three concurrent tasks (Payment, Mail, Page) print timestamps while holding locks:
- Payment: Holds lock during entire operation (serialized access)
- Mail & Page: Brief synchronization, then independent work
```

**When to Use:**

- Updating shared data structures (counters, lists, dictionaries)
- Writing to the same file from multiple threads
- Managing resource pools or connection limits

**Additional Synchronization Primitives:**

- **Semaphore:** Like a locker room with N available lockers. Multiple threads can access up to N resources concurrently.
- **Condition Variable:** A waiting area where threads can wait for a signal before proceeding.
- **Event:** A flag that threads can wait for or set to coordinate actions.

---

### 3. `3_multiprocessing.py` - Parallel Processing with Multiple Processes

**Purpose:** Demonstrates true parallelism using separate processes that can run on multiple CPU cores.

**Key Concepts:**

- Creating separate processes with `multiprocessing.Process`
- Independent memory spaces per process (no shared memory by default)
- `start()` and `join()` for process management
- GIL-free execution for CPU-bound tasks
- Process naming and identification

**Key Difference from Threading:**

> Each process has its own Python interpreter and memory space, enabling true parallel execution on multi-core systems without GIL limitations.

**Use Case:** CPU-bound operations that don't share memory.

**Example Scenario:**

```
Two independent processes calculate and log timestamps:
- Process-1: Operates completely independently
- Process-2: Has separate memory, runs truly in parallel on different CPU cores
```

**Important Note:** The `if __name__ == "__main__":` guard is **required** on Windows and macOS to prevent recursive process spawning.

**When to Use:**

- Image processing pipelines
- Data analysis on large datasets
- Scientific computations
- Machine learning model training
- Embarrassingly parallel problems with no data sharing

**Overhead:** Multiprocessing has higher startup and memory overhead than threading, so use only when benefits justify the cost.

---

### 4. `4_asyncio.py` - Async I/O with Event Loop

**Purpose:** Demonstrates non-blocking concurrent I/O using Python's asyncio library.

**Key Concepts:**

- Coroutines with `async def` and `await`
- Event loop for managing concurrent execution
- `asyncio.gather()` for running multiple coroutines
- Yielding control with `await asyncio.sleep()`
- Single-threaded concurrency without thread overhead

**How It Works:**

> A single thread manages an event loop. When a coroutine hits an `await` statement, it yields control to allow other coroutines to run. No context switching overhead like with threads.

**Use Case:** High-concurrency I/O operations with minimal overhead.

**Example Scenario:**

```
Three concurrent tasks with different delays run concurrently:
- Task-A: 1.0s delay × 5 = ~5s normally
- Task-B: 2.0s delay × 5 = ~10s normally
- Task-C: 1.5s delay × 4 = ~6s normally

But they run concurrently, so total time ≈ 10s (max of all tasks)
instead of 21s (sum of all tasks)
```

**When to Use:**

- Web servers handling thousands of concurrent clients
- API clients making many simultaneous requests
- Real-time data streaming
- Chat applications or live updates
- Database query handling

**Performance Benefit:** Can handle tens of thousands of concurrent connections with minimal resource usage.

---

## Quick Comparison: When to Use Each

### Use **Threading** (`1_basic_threading.py`, `2_lock_threading.py`) when:

- ✅ Tasks are **I/O-bound** (network, files, databases)
- ✅ You need **simple data sharing** between tasks
- ✅ You have **a few tasks** (dozens, not thousands)
- ✅ You need **blocking operations** that work with threading
- ⚠️ Limited by Python's GIL on CPU-bound work

**Example:** Web scraper fetching 10-20 URLs concurrently

### Use **Multiprocessing** (`3_multiprocessing.py`) when:

- ✅ Tasks are **CPU-bound** (calculations, processing)
- ✅ You have **multiple CPU cores**
- ✅ Tasks need **isolated memory spaces**
- ✅ You can afford **higher overhead** (startup, memory)
- ⚠️ More complex to coordinate between processes

**Example:** Processing 1000 images in parallel on a 16-core machine

### Use **Asyncio** (`4_asyncio.py`) when:

- ✅ Tasks are **I/O-bound** with **many concurrent operations**
- ✅ You want **minimal overhead** (single thread)
- ✅ You're working with **async-friendly libraries** (aiohttp, asyncpg)
- ✅ You need to handle **thousands of concurrent connections**
- ⚠️ Requires rewriting code to use `async/await`

**Example:** Web server handling 10,000 concurrent client requests

---

## Synchronization Primitives Explained

### Lock (Mutex)

```
🚪 Public Restroom
Only 1 person can use at a time. Others wait in queue.
Use: Protecting critical sections of code
```

### Semaphore

```
🗂️ Locker Room
10 lockers available. Up to 10 people can use simultaneously.
Counter decrements on acquire, increments on release.
Use: Limiting resource access (e.g., DB connection pool with 10 connections)
```

### Condition Variable

```
⏳ Waiting Area with Call Button
Threads wait on a condition (e.g., "is data available?").
When condition is met, notifier signals waiting threads to proceed.
Use: Producer-consumer patterns, thread coordination
```

### Event

```
🚩 Flag Signal
Simple on/off state. Threads wait for flag to be set.
Use: Signaling thread shutdown, synchronizing group actions
```

---

## Common Patterns

### Pattern 1: Threading with Locks (Producer-Consumer)

```python
# Thread 1: Producer writes to shared queue with lock
lock.acquire()
shared_queue.append(data)
lock.release()

# Thread 2: Consumer reads from shared queue with lock
lock.acquire()
data = shared_queue.pop(0)
lock.release()
```

### Pattern 2: Multiprocessing with Pool

```python
from multiprocessing import Pool
with Pool(4) as pool:  # 4 worker processes
    results = pool.map(cpu_bound_function, data_list)
```

### Pattern 3: Asyncio with Gather

```python
async def main():
    results = await asyncio.gather(
        async_task_1(),
        async_task_2(),
        async_task_3()
    )
```

---

## Running the Examples

```bash
# Basic threading
python3 1_basic_threading.py

# Threading with locks
python3 2_lock_threading.py

# Multiprocessing (requires if __name__ guard)
python3 3_multiprocessing.py

# Asyncio
python3 4_asyncio.py
```

---

## Performance Tips

1. **Threading:** Use for I/O-bound tasks; avoid busy loops
2. **Multiprocessing:** Use for CPU-bound tasks; consider process pools
3. **Asyncio:** Use for I/O-bound tasks with many concurrent operations; leverage async libraries

---

## Further Reading

- [Python threading documentation](https://docs.python.org/3/library/threading.html)
- [Python multiprocessing documentation](https://docs.python.org/3/library/multiprocessing.html)
- [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html)
- [Real Python - Threading vs Multiprocessing](https://realpython.com/intro-to-python-threading/)
- [Real Python - Async IO](https://realpython.com/async-io-python/)
