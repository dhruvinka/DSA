from CirculerQ import *

class PQUsingArray:

    def __init__(self):
        self.q1 = CircularQ(5)
        self.q2 = CircularQ(5)
        self.q3 = CircularQ(5)

    def insert(self, data, pri):
        if pri not in [1,2,3]:
            print("Invalid Priority")
            return
        
        if pri == 1:
            if self.q1.is_full():
                print("Priority 1 Queue Full")
            else:
                self.q1.enqueue(data)

        elif pri == 2:
            if self.q2.is_full():
                print("Priority 2 Queue Full")
            else:
                self.q2.enqueue(data)

        elif pri == 3:
            if self.q3.is_full():
                print("Priority 3 Queue Full")
            else:
                self.q3.enqueue(data)

    def delete(self):
        if not self.q1.is_empty():
            return self.q1.dequeue()
        elif not self.q2.is_empty():
            return self.q2.dequeue()
        elif not self.q3.is_empty():
            return self.q3.dequeue()
        else:
            print("Queue Empty")
            return None
        
if __name__ == "__main__":
    pq=PQUsingArray()
    pq.insert("Task1", 2)
    pq.insert("Task2", 1)
    pq.insert("Task3", 3)
    print(pq.q1.queue)
    print(pq.q2.queue)
    print(pq.q3.queue)
    pq.delete()
    print(pq.q1.queue)
    print(pq.q2.queue)
    print(pq.q3.queue)
    pq.delete()
    print(pq.q1.queue)
    print(pq.q2.queue)
    print(pq.q3.queue)