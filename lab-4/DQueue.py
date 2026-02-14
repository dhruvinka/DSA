# DQueue
from collections import deque
class DQueue:
    def __init__(self,size):
        self.q=[None]*size
        self.f=-1
        self.r=-1
        self.size=size
    
    def is_full(self):
        return self.r == self.size-1
    
    def is_empty(self):
        return self.f==-1 or self.f > self.r
    
    def Enqueue_At_rear(self,val):
        if self.is_full():
            print("Queue is Full")
        else:
            if self.f==-1:
                self.f+=1
            self.r+=1
            self.q[self.r]=val

    def Enqueue_At_front(self,val):
        if self.is_full():
            print("Queue is Full")
        else:
            if self.f==-1:
                self.f=0
                self.r=0
                self.q[self.f]=val
            else:
                self.f-=1
                self.q[self.f]=val

    def Dequeue_At_front(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            val=self.q[self.f]
            self.q[self.f]=None
            self.f+=1
            return val
    def Dequeue_At_rear(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            val=self.q[self.r]
            self.q[self.r]=None
            self.r-=1
            return val
    def display(self):
        print(self.q)
        print(self.f)
        print(self.r)
s=DQueue(5)
s.Enqueue_At_rear(1)
s.display()
s.Enqueue_At_rear(2)
s.display()
s.Enqueue_At_rear(3)
s.display()

s.Enqueue_At_front(4)
s.display()

s.Enqueue_At_front(5)
s.display()
s.Dequeue_At_front()
s.display()

s.Dequeue_At_rear()
s.display()
    