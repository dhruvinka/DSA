from CirculerQ import CirculerQ

class Pq:
    def __init__(self,size):
        self.q1=CirculerQ(size)
        self.q2=CirculerQ(size)
        self.q3=CirculerQ(size)

    def is_full(self):
        return self.q1.is_full() and self.q2.is_full() and self.q3.is_full()
    
    def is_empty(self):
        return self.q1.is_empty() and self.q2.is_empty() and self.q3.is_empty()
    
    def enqueue(self,data,priority):
        if self.is_full():
            print("pq is full")
            return
        if priority in[1,2,3]:
            if priority == 1:
                if self.q1.is_full():
                    print("q1 is full")
                    return
                else:
                    self.q1.enqueue(data)
            elif priority==2:
                if self.q2.is_full():
                    print("q2 is full")
                    return
                else:
                    self.q2.enqueue(data)
            else:
                if self.q3.is_full():
                    print("q3 is full")
                    return
                else:
                    self.q3.enqueue(data)
        else:
            print("invalid priority")

    def dequeue(self):
        if self.is_empty():
            print("pq is empty")
            return
        if not self.q1.is_empty():
            return self.q1.dqueue()
        elif not self.q2.is_empty():
            return self.q2.dqueue()
        else:
            return self.q3.dqueue()
        
if __name__ == "__main__":
    p=Pq(5)
    p.enqueue(1,1)
    p.enqueue(2,1)
    p.enqueue(3,2)
    p.enqueue(4,3)
    p.enqueue(5,3)
    print(p.q1.queue,p.q2.queue,p.q3.queue)
    print(p.dequeue())
    print(p.dequeue())
    print(p.dequeue())
    print(p.q1.queue,p.q2.queue,p.q3.queue)


        