class Queue:
    def __init__(self, size):
        self.size = size
        self.r = -1
        self.f = -1
        self.q = [None] * self.size

    def is_full(self):
        return (self.r + 1) % self.size == self.f

    def is_Empty(self):
        return self.f == -1

    def Enqueue(self, val):
        if self.is_full():
            print("Queue is Full")
        else:
            if self.f == -1:  
                self.f = 0
            
            self.r = (self.r + 1) % self.size
            self.q[self.r] = val

    def Dequeue(self):
        if self.is_Empty():
            print("Queue is Empty")
            return None
        
        val = self.q[self.f]
        self.q[self.f] = None
        
        if self.f == self.r: 
            self.f = -1
            self.r = -1
        else:
            self.f = (self.f + 1) % self.size
        return val

    def display(self): 
        print(f"Front: {self.f}, Rear: {self.r}")
        print(f"Queue: {self.q}")
        print("-" * 20)

if __name__ == "__main__": 
    s = Queue(5)
    s.Enqueue(10)
    s.Enqueue(20)
    s.Enqueue(30)
    s.Enqueue(40)
    s.Enqueue(50)
    s.display()
    
    s.Dequeue()
    s.Dequeue()
    s.display()
    
    s.Enqueue(60) 
    s.display()