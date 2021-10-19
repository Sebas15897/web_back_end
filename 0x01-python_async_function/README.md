###  ⚡0x01. Python - Async ⚡

### Author

Sebastián Contreras / sebastiancontreras15897@gmail.com 📧

--------------------------------------------------------
### Web developer 💻

By learning related concepts, we explain step by step what asynchronous programming is.

1.1 blocking
Suspended state when the program does not get the necessary computing resources.
While a program is waiting for an operation to complete, it cannot continue doing other things, the program is said to be stuck in the operation.
Common forms of blocking are: network I / O blocking, disk I / O blocking, user input blocking, and so on.
Blocking is ubiquitous, even when the CPU switches context, all processes can't really do things, and they are also blocked. (If it is a multi-core CPU, the core that performs the context switch operation cannot be used.)

1.2 No blocking
When a program is waiting for an operation, it is not blocked and can continue to do other things. The program is said to be not blocking on this operation.
No lock Is not Can exist at any program level and under any circumstances.
A non-blocking state is only possible if the encapsulation level of the program can include independent subroutine units.
The existence of non-blocking is because the blocking exists. Precisely because of blocking a time-consuming and inefficient operation, we have to do it without blocking.

1.3 Synchronization
To complete a task, different program units depend on a certain communication method to coordinate. These program units are said to run synchronously.
For example, to update the inventory of goods in a purchasing system, it is necessary to use "row lock" as a communication signal to force different update requests to be queued for sequential execution. The inventory update operation is synchronized.
In short Synchronization means order。
1.4 asynchronous
To perform a task, between different program units
Irrelevant program units can be asynchronous.
For example, a crawler downloads a web page. After the scheduler calls the downloader, other tasks can be scheduled without having to contact the download task to coordinate the behavior. The download and save operations of different web pages are irrelevant, and there is no need to notify each other to coordinate. The timing of the completion of these asynchronous operations is uncertain.
In short Asynchronous means out of order。
The "communication method" mentioned above generally refers to the synchronization primitives provided by asynchronous and concurrent programming, such as semaphores, locks, synchronous queues, and so on. run synchronously under certain conditions, they are necessary due to their asynchronous existence. If all the programs run in sequence, they are synchronized, then why do they need these synchronization signals?

### 💻#end💻
