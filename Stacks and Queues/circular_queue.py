# ----------------------------------------
# Circular Queue (Ring Buffer) in Python
# ----------------------------------------

class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.size = k
        self.front = 0
        self.rear = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


# ----------------------------------------
# Example Usage
# ----------------------------------------

if __name__ == "__main__":
    q = MyCircularQueue(3)
    print(q.enQueue(1))  # True
    print(q.enQueue(2))  # True
    print(q.enQueue(3))  # True
    print(q.enQueue(4))  # False (full)
    print(q.Rear())      # 3
    print(q.isFull())    # True
    print(q.deQueue())   # True
    print(q.enQueue(4))  # True (wraps around)
    print(q.Rear())      # 4
