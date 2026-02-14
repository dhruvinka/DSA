from  Circuler import *

class PriorityQueue:
    def __init__(self):
        self.q1=Queue(5)
        self.q2=Queue(5)
        self.q3=Queue(5)

    def Enqueue(self,val,priority):

        if priority==1:
            if self.q1.is_full():
                print("Priority 1 Queue is Full")
            else:
                self.q1.Enqueue(val)
        elif priority==2:
            if self.q2.is_full():
                print("Priority 2 Queue is Full")
            else:
                self.q2.Enqueue(val)
        elif priority==3:
            if self.q3.is_full():
                print("Priority 3 Queue is Full")
            else:
                self.q3.Enqueue(val)

    def Dequeue(self):
        if not self.q1.is_Empty():
            print("Dequeue from Priority 1 Queue value is :",self.q1.Dequeue())
        elif not self.q2.is_Empty():
            print("Dequeue from Priority 2 Queue value is :",self.q2.Dequeue())
        elif not self.q3.is_Empty():
            print("Dequeue from Priority 3 Queue value is :",self.q3.Dequeue())
        else:
            print("All Queues are Empty")
            
    def display(self):
        print("Priority 1 Queue:")
        self.q1.dislay()
        print("Priority 2 Queue:")
        self.q2.dislay()
        print("Priority 3 Queue:")
        self.q3.dislay()

__name__="__main__"
s=PriorityQueue()
s.Enqueue(1,1)
s.Enqueue(2,1)
s.Enqueue(3,2)
s.Enqueue(4,2)
s.Enqueue(5,3)
s.Enqueue(6,3)
s.Enqueue(7,3)

s.Dequeue()
s.Dequeue()
s.Dequeue()
s.Dequeue()
s.Dequeue()
s.Dequeue()
s.Dequeue()
s.Dequeue()
s.display()
     

        
