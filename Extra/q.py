# class Q:
#     def __init__(self, size):
#         self.size = size
#         self.queue = [None] * size
#         self.f = -1
#         self.r = -1

#     def is_Empty(self):
#         return self.f == -1 and self.r == -1

#     def is_Full(self):
#         return self.r == self.size - 1

#     def push(self, val):
#         if self.is_Full():
#             print("Queue is Full")
#             return

#         if self.f == -1:
#             self.f = 0

#         self.r += 1
#         self.queue[self.r] = val

#     def pop(self):
#         if self.is_Empty():
#             print("Queue is Empty")
#             return

#         val = self.queue[self.f]
#         if self.f == self.r:
#             self.f = -1
#             self.r = -1
#         else:
#             self.f += 1

#         return val

#     def peek(self):
#         if self.is_Empty():
#             return None
#         return self.queue[self.f]

#     def display(self):
#         print("Queue:", self.queue)
#         print("Front:", self.f)
#         print("Rear:", self.r)

#     def destroy(self):
#         self.f = None
#         self.r = None
#         self.queue = None   
#         self.size = None


class Q:
    def __init__(self,size):
        self.r=-1
        self.f=-1
        self.queue=[]
        self.size=size

    def is_Full(self):
        if self.r == self.size-1:
            return True
        return False

    def is_Empty(self):
        if self.r ==-1 and self.f == -1:
            return True
        return False
    
    def push(self,val):
        if self.is_Full():
            print("Queue is Full")
            return
        self.queue.append(val)
        self.r+=1

        if self.f == -1:
            self.f=0

    def pop(self):
        if self.is_Empty():
            print("Queue is Empty")
            return
        self.queue.pop(0)
        self.r-=1
        if (self.r ==self.f):
            self.r=-1
            self.f=-1
        
    def peek(self):
        if self.is_Empty():
            print("Queue is Empty")
        return self.queue[0]
    
    def display(self):
        print("Queue:", self.queue)
        print("Front:", self.f)
        print("Rear:", self.r)
    