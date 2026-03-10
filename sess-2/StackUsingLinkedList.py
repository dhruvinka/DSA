from Node import *;


class Stack:
    def __init__(self):
        self.head=None
        self.size=0

    def push(self,data):

        if self.head is None:
            new_node=Node(data)
            self.head=new_node
            self.size+=1
        else:
            new_node=Node(data)
            curr=self.head
            while curr.next != None:
                curr=curr.next
            curr.next=new_node
            self.size+=1

    def pop(self):

        if  self.head is None:
            return 
        if self.head.next is None:
            data=self.head.data
            self.head=None
            return data
        
        curr=self.head
        prev=None
        while curr.next != None:
            prev=curr
            curr=curr.next
        data=curr.data
        prev.next=None
        return data
    
    def peek(self):

        if  self.head is None:
            return 
        curr=self.head
        while curr.next != None:
            curr=curr.next
        data=curr.data
        return data
    
l1=Stack()
l1.push(10)
l1.push(20)
l1.push(30)
print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1.peek())
    
         



        