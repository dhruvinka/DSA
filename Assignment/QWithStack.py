# 6. Write a program to Implement a simple Queue using stack data structure. 

from S import *

class Q:
    def __init__(self,size):
        self.s1=Stack(size)
        self.s2=Stack(size)
        self.f=-1
        self.r=-1
        self.size=size

    def is_full(self):
         return self.r == self.size - 1
    
    def is_Empty(self):
         return self.f == -1 and self.r==-1
         

    def enqueue(self,data):
        if self.is_full():
            print("Full")
        else:  
            if self.f==-1:
                self.f+=1
        
            self.r+=1
            self.s1.push(data)

    def dqueue(self):
            if self.is_Empty():
                print("Empty")
            else:
                if self.f == self.r:
                    self.f==-1
                    self.r==-1

                while not len(self.s1.s) == 0:
                        self.s2.push(self.s1.pop())
                x =self.s2.pop()
                while not len(self.s2.s) == 0:
                        self.s1.push(self.s2.pop())
                self.f+=1
                    
                return x
                

    def display(self):
        self.s1.display()
        # self.s2.display()
        # print(self.f,self.r)


if __name__=="__main__":
    q1=Q(5)
    q1.enqueue(30)
    q1.enqueue(40)
    print('d 30',q1.dqueue())
    q1.enqueue(50)
    q1.enqueue(60)
    print('d 40',q1.dqueue())
    q1.enqueue(70)
    print('d 50',q1.dqueue())
    print('d 60',q1.dqueue())
    print('d 70',q1.dqueue())
    q1.enqueue(80)
    q1.display()


        