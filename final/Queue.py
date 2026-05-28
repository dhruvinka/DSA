class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1


    def is_full(self):
        return self.rear==self.size-1
    
    def is_empty(self):
        return self.front==-1
    
    def enqueue(self,data):
        if self.is_full():
            print("Q is full")
        else:
            if self.front==-1:
                self.front=0
            self.rear+=1
            self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Q is empty")
        else:
            data=self.queue[self.front]
            self.queue.pop(self.front)
            self.rear-=1
            if self.rear==-1:
                self.front=-1
            return data
        
if __name__ == "__main__":
    q=Queue(5)
    q.enqueue(1)
    q.enqueue(2)   
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.queue)
    print(q.dequeue())
    print(q.dequeue())
    print(q.queue)