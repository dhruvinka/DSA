

class Person :

    def __init__(self,size):
        self.size=size
        self.r=-1
        self.f=-1
        self.q=[None]*self.size
        self.total=20

    def is_full(self):
        return (self.r+1) % self.size == self.f
    
    def is_Empty(self):
         return  self.f == -1
    
    def Enqueue(self,val,tick):
        if self.is_full():
            print("Queue is Full")
        else:
            if self.f == -1:
                self.f = 0
            
            self.r = (self.r + 1) % self.size
            self.q[self.r] = (val,tick)

    def Dequeue(self):
        if self.is_Empty():
            print("Queue is Empty")
        else:
            val = self.q[self.f]
            self.q[self.f] = None

            if self.f == self.r:
                self.f = -1
                self.r = -1
            else:
                self.f = (self.f + 1) % self.size

            return val

    def dislay(self):
        print(self.f)
        print(self.r)
        print(self.q)

    
    def enterintoQ(self,name,tickets):
        self.Enqueue(name,tickets)

    def processQ(self):
        x=self.Dequeue()
        print(x)
        if self.total >= int(x[1]):
            self.total -=int(x[1])
            print("total Aval Tik",self.total)
        else:
            print("Soory..")


        
p1=Person(10)
p1.enterintoQ('rema',20)
p1.enterintoQ('kanani',5)
p1.processQ()
p1.processQ()



