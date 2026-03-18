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
            new_node.next=self.head
            self.head=new_node
            self.size+=1

    def pop(self):
        if self.size > 0:
            if self.head.next is None:
                data=self.head.data
                self.head=None
                self.size-=1
                return data
            else:
                data=self.head.data
                self.head=self.head.next
                self.size-=1
                return data
        else:
              print("No element Left")
    
    def peek(self):
        if self.size > 0:
            curr=self.head
            while curr.next != None:
                curr=curr.next
            data=curr.data
            return data
        else :
            print("No element Left in Stack")
    
l1=Stack()
l1.push(10)
l1.push(20)
l1.push(30)
print(l1.pop())
print(l1.pop())
print("Peek",l1.peek())
print(l1.pop())
print(l1.pop())
print(l1.pop())
    
         



        