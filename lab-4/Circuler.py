class Queue:

    def __init__(self,size):
        self.size=size
        self.r=-1
        self.f=-1
        self.q=[None]*self.size

    def is_full(self):
        return (self.r+1) % self.size == self.f
    
    def is_Empty(self):
         return  self.f == -1
    
    def Enqueue(self,val):
        if self.is_full():
            print("Queue is Full")
        else:
            if self.f == -1:
                self.f+=1
            if self.r==self.size-1 and self.f!=0:
                 self.r=0
                 self.q[self.r]=val
            else:
                self.r+=1
                self.q[self.r]=val

    def Dequeue(self):
        if self.is_Empty():
            print("Queue is Empty")
        else:
            if self.f == self.r:
                val =self.q[self.f]
                self.q[self.f]=None
                self.f=-1
                self.r=-1
            else:
                val =self.q[self.f]
                self.q[self.f]=None
                self.f+=1
            return val

    def dislay(self):
        print(self.f)
        print(self.r)
        print(self.q)


# __name__="__main__"
# s=Queue(5)
# s.Enqueue(1)
# s.Enqueue(1)
# s.Enqueue(1)
# s.Enqueue(1)
# s.Enqueue(1)
# s.Enqueue(1)
# s.dislay()
# s.Dequeue()
# s.Dequeue()
# s.Dequeue()
# s.Dequeue()
# s.Dequeue()
# s.Dequeue()
# s.dislay()





