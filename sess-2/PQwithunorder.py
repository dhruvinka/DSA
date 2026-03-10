class PQwithunorder():

    def __init__(self):
        self.q=[]

    def is_empty(self):
        return len(self.q)==0
    
    def enqueue(self,data,priority):
        if 1 <= priority <= 3:
            self.q.append((data,priority))
        else:
            print("Enter priority between 1 and 3")
    
    def dequeue(self):
        
        if self.is_empty():
            print("Queue is Empty")
            return
        
        for i in range(len(self.q)):
            if self.q[i][1] == 1:
                return self.q.pop(i)

        for i in range(len(self.q)):
            if self.q[i][1] == 2:
                return self.q.pop(i)

        for i in range(len(self.q)):
            if self.q[i][1] == 3:
                return self.q.pop(i)

    def display(self):
        if self.is_empty():
            print("Q is Empty")
        else:
            print("Queue:", self.q)


if __name__ == "__main__":

    q=PQwithunorder()

    q.enqueue("A",1)
    q.enqueue("B",2)    
    q.enqueue("C",2)    
    q.enqueue("D",1)    
    q.enqueue("E",3)
    q.enqueue("F",5)

    q.display()

    print("Dequeue:",q.dequeue())    
    print("Dequeue:",q.dequeue())    
    print("Dequeue:",q.dequeue())    
    print("Dequeue:",q.dequeue())
    print("Dequeue:",q.dequeue())
    print("Dequeue:",q.dequeue())

    q.display()