from CirculerQ import *

class PQUsingSortedQ:
    def __init__(self):
        self.q = [] 
        self.size = 5
        self.front = -1
        self.rear = -1

    def is_full(self):
        return len(self.q) == self.size
    
    def is_empty(self):
        return len(self.q) == 0
    
    def insert(self, data,priority):
        if self.is_full():
            print("Queue is full")
            return
        else:
            if priority not in [1,2,3]:
                print("Invalid priority")
                return
            else:
                if self.front == -1:
                    self.front = 0
                self.rear += 1
                self.q.append((data, priority))
            
            

    def delete(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            for i in range(len(self.q)):
                if self.q[i][1] == 1:
                    data = self.q[i][0]
                    self.q.pop(i)       
                    return data
                
            for i in range(len(self.q)):
                if self.q[i][1] == 2:
                    data = self.q[i][0]
                    self.q.pop(i) 
                    return data
                
            for i in range(len(self.q)):
                if self.q[i][1] == 3:
                    data = self.q[i][0]
                    self.q.pop(i) 
                    return data
                
if __name__ == "__main__":
    pq = PQUsingSortedQ()
    pq.insert("Task1", 2)
    pq.insert("Task2", 1)
    pq.insert("Task3", 3)
    print(pq.q)
    print(pq.delete())  
    print(pq.delete())  
    print(pq.delete())  
            

   