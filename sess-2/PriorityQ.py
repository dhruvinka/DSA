from Q import *;


class PriorityQ:
    #  used circuler Q
    def __init__(self):
        self.q1=SimpleQueue(6)
        self.q2=SimpleQueue(6)
        self.q3=SimpleQueue(6)

    def Enqueue(self,val,priority):

        if priority == 1:
            if self.q1.is_full():
                print("Priority 1 Queue is Full")
            else:
                self.q1.enqueue(val)
        elif priority==2:
            if self.q2.is_full():
                print("Priority 2 Queue is Full")
            else:
                self.q2.enqueue(val)
        elif priority==3:
            if self.q3.is_full():
                print("Priority 3 Queue is Full")
            else:
                self.q3.enqueue(val)
                

    def Dequeue(self):

        if not self.q1.is_empty():
            print("Dequeue from Priority 1 Queue value is :",self.q1.dequeue())
           
        elif not self.q2.is_empty():
            print("Dequeue from Priority 2 Queue value is :",self.q2.dequeue())
           
        elif not self.q3.is_empty():
            print("Dequeue from Priority 3 Queue value is :",self.q3.dequeue())
            
        else:
            print("no Element in Queue")


    def display(self):
        print("Priority 1 Queue:")
        self.q1.display()
        print("Priority 2 Queue:")
        self.q2.display()
        print("Priority 3 Queue:")
        self.q3.display()

__name__="__main__"
s=PriorityQ()
s.Enqueue(1,1)
s.Enqueue(2,1)
s.Enqueue(10,2)
s.Enqueue(50,1)
s.Enqueue(50,3)
s.display()
s.Dequeue()
s.Dequeue()
s.Dequeue()
s.Dequeue()
s.Dequeue()