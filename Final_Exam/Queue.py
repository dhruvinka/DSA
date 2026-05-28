class Queue:
    def __init__(self,size):
        self.queue=[False]*size
        self.size=size
        self.front=-1
        self.rear=-1

    def is_empty(self):
        return self.front==-1 and self.rear==-1
    
    def is_full(self):
        return self.rear==self.size-1
    
    def enqueue(self,data):
        if self.is_full():
            print("Queue is full")
        else:
            if self.front==-1:
                self.front+=1
            self.rear+=1
            self.queue[self.rear]=data

    def dequeue(self):
        if self.is_empty():
            print("Empty")
        else:
            data=self.queue[self.front]
            self.queue[self.front]=False
            if self.front==self.rear:
                self.front=-1
                self.rear=-1
            else:
                self.front+=1
            return data
        
    def peek(self):
        if self.is_empty():
            print("Empty")
        else:
            data=self.queue[self.front]
            self.queue[self.front]=False
            return data
        

if __name__ == "__main__":
    q=Queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q.peek())
    print(q.dequeue())
    print(q.peek())
    print(q.queue)