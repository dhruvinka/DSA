
class SimpleQueue:
    def __init__(self,size):
        self.r=-1
        self.f=-1
        self.q=[None]*size
        self.size=size

    def is_full(self):
        return self.r==self.size-1 
    
    def is_empty(self):
        return self.f==-1 or self.r==-1
    
    def enqueue(self,data):
        if self.is_full():
            print("Queue is full")
        else:
            if self.f==-1:
                self.f=0
            self.r+=1
            self.q[self.r]=data
    
    def dequeue(self):
        if self.is_empty():
            print("Q is Empty")
        else:
            data=self.q[self.f]
            if self.f == self.r:
                self.f=-1
                self.r=-1
            else:
                self.f+=1
            return data
        
    def peek(self):
        if self.is_empty():
            print("Q is Empty")
        else:
            return self.q[self.f]
        
    def display(self):
        if self.is_empty():
            print("Q is Empty")
        else:
            print("Queue:", end=" ")
            print(self.q)
            print("Front:", self.f)
            print("Rear:", self.r)
            




