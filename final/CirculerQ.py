class CircularQ:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.is_full():
            print("Overflow")
            return
        
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Underflow")
            return
        
        x = self.queue[self.front]
        self.queue[self.front] = None
        
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        return x

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def display(self):
        print(self.queue)

# if __name__ == "__main__":
#     cq = CircularQ(5)
#     cq.enqueue(1)
#     cq.enqueue(2)
#     cq.enqueue(3)
#     cq.enqueue(4)   
#     cq.enqueue(5)
#     cq.display()
#     print(cq.dequeue())
#     cq.display()
#     print(cq.dequeue())
#     cq.display()
#     cq.enqueue(6)
#     cq.display()