class CirculerQ:
    def __init__(self,size):
        self.size=size
        self.queue=[False]*size
        self.r=-1
        self.f=-1

    def is_full(self):
        return (self.r+1) % self.size == self.f
        
    def is_empty(self):
        return self.f==-1
    
    def enqueue(self,data):
        if self.is_full():
            print("q is full")
        else:
            if self.f == -1:
                self.f=0
            
            self.r=(self.r+1) % self.size
            self.queue[self.r]=data
    
    def dqueue(self):
        if self.is_empty():
            print("empty")
        else:
            val=self.queue[self.f]
            self.queue[self.f]=None

            if self.f == self.r:
                self.f=-1 
                self.r=-1
            else:
                self.f=(self.f+1) % self.size
        return val

if __name__ == "__main__":

    q=CirculerQ(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.queue)
    q.enqueue(6)
    print(q.dqueue())
    q.enqueue(6)
    print(q.queue)
    print(q.dqueue())
    q.enqueue(6)
    print(q.dqueue())
    print(q.queue)


