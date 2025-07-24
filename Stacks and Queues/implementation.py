# ------------------------------
# Stack and Queue Implementations in Python
# ------------------------------

# ------------------------------
# Stack using Python List
# ------------------------------

print("=== Stack (LIFO) Implementation ===")

stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)

# Pop element
top = stack.pop()
print("Popped element:", top)
print("Stack after pop:", stack)

# Peek at the top element
if stack:
    print("Top element:", stack[-1])
else:
    print("Stack is empty")

print()  # Separator

# ------------------------------
# Queue using List (not efficient)
# ------------------------------

print("=== Queue (FIFO) using List (inefficient) ===")

queue = []

# Enqueue elements
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueues:", queue)

# Dequeue element
front = queue.pop(0)
print("Dequeued element:", front)
print("Queue after dequeue:", queue)

print()  # Separator

# ------------------------------
# Queue using deque (efficient)
# ------------------------------

from collections import deque

print("=== Queue (FIFO) using deque (recommended) ===")

queue = deque()

# Enqueue elements
queue.append(100)
queue.append(200)
queue.append(300)
print("Queue after enqueues:", queue)

# Dequeue element
front = queue.popleft()
print("Dequeued element:", front)
print("Queue after dequeue:", queue)

# ----------------------------------------
# Stack and Queue Implementation Using Linked Lists
# ----------------------------------------

# Node class (used for both Stack and Queue)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ----------------------------------------
# Stack Implementation (LIFO)
# ----------------------------------------

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.top is None

    def display(self):
        temp = self.top
        print("Stack (top -> bottom):", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# ----------------------------------------
# Queue Implementation (FIFO)
# ----------------------------------------

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return None
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed

    def is_empty(self):
        return self.front is None

    def display(self):
        temp = self.front
        print("Queue (front -> rear):", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# ----------------------------------------
# Demo
# ----------------------------------------

print("=== Stack Using Linked List ===")
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped:", s.pop())
s.display()
print("Peek:", s.peek())

print("\n=== Queue Using Linked List ===")
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print("Dequeued:", q.dequeue())
q.display()
