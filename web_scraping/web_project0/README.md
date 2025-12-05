# MultiThreadingPython

## Lock Objects, Semaphores, Condition Variables

#### Imagine a public restroom with a single lock on the door (lock object). Only one person can enter at a time, ensuring privacy.
#### Now, consider a locker room with 10 lockers (semaphore). Multiple people can access lockers concurrently as long as there are lockers available (counter > 0).
#### Finally, think of a waiting area with chairs and a call button (condition variable). People waiting for a locker can sit and wait (holding a lock on the waiting area). When a locker becomes available, someone can press the call button (notify) to signal a waiting person (who can then acquire the locker).

Here's a breakdown of when to use the multiprocessing module vs. the threading module in Python:
## Use multiprocessing when:
Your tasks are CPU-bound: This means the tasks spend most of their time performing calculations and not waiting for external resources (like I/O operations).
You have multiple CPU cores: Since multiprocessing leverages separate processes, it can truly take advantage of multiple cores to achieve parallel execution.
You need to isolate tasks: Processes have separate memory spaces, which can be helpful for tasks that might have memory leaks or require isolated environments.

## Use threading when:
Your tasks are I/O-bound: This means the tasks spend a significant amount of time waiting for external resources like network requests, disk access, or user input. In these scenarios, threads can improve responsiveness by allowing other threads to execute while one thread waits for I/O.
You have a single CPU core: While threading can still help with I/O-bound tasks even on a single core, the benefits of true parallelism won't be realized.
You need to share data between tasks: Threads within the same process share memory, making it easier to directly access and modify shared data structures. However, be cautious of race conditions and use appropriate synchronization mechanisms (locks) when modifying shared data.

In essence, choose multiprocessing for true parallel processing on CPU-bound tasks with multiple cores, and use threading for I/O-bound tasks or when data sharing between threads is necessary.
