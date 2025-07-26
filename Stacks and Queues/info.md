# STACKS AND QUEUES

Stack and Queue are two data structures where the processing order is restricted.

They are both linear data structures and are flexible with their sizes.

The difference comes in how elements are removed from them. 

**STACK - LIFO (Last In First Out)**

eg: A stack of dishes. 

**QUEUE - FIFO (First In First Out)**

eg: A queue of people at the ticket counter. 

[IMPLEMENTATION](implementation.py)

# CIRCULAR QUEUE
In a naive queue implementation using a fixed-size array, we typically use two pointers: one to track the front (start) and another for the end (end) of the queue. When we enqueue elements, they are added at the end, and when we dequeue, the start pointer moves forward. However, a major drawback arises when the end reaches the array's capacity — even if we've dequeued elements and there is space at the beginning of the array, new elements can't be enqueued because the queue doesn't wrap around. This leads to wasted space and inefficient memory use, especially in limited-size environments. A circular queue can solve this issue by reusing the freed space.

This drawback can be seen in this example: 

Enqueued 1 -> [1, None, None, None, None]

Enqueued 2 -> [1, 2, None, None, None]

Enqueued 3 -> [1, 2, 3, None, None]

Enqueued 4 -> [1, 2, 3, 4, None]

Enqueued 5 -> [1, 2, 3, 4, 5]

Dequeued 1 -> [None, 2, 3, 4, 5]

Dequeued 2 -> [None, None, 3, 4, 5]

Cannot enqueue 6: Queue is 'full' (end reached)

Cannot enqueue 7: Queue is 'full' (end reached)

A Circular Queue, also known as a Ring Buffer, is a linear data structure that uses a fixed-size array in a circular manner. Unlike a traditional queue, it efficiently reuses the space of dequeued elements. When the rear of the queue reaches the end of the array, it wraps around to the front if there is space.


This design solves the issue of wasted space in naive array-based queues and supports constant-time enqueue and dequeue operations.

[Circular Queue IMPLEMENTATION](circular_queue.py)

[Explore Stacks and Queues](https://leetcode.com/explore/learn/card/queue-stack/)