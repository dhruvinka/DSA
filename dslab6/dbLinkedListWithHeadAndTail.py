# 2. Implement the following features for a doubly linked list with head and tail pointer
# library.
# a. Create an Empty List
# b. Inserting Node
# i. as First Node,
# ii. as Last Node,
# c. Deleting Node
# i. at First,
# ii. at Last,
# d. Display/ Traverse List
# i. Forward
# ii. Reverse
# e. Size of linked list

from DbNode import *;

class dbLinkedListWithHeadAndTail:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def insert_At_beg(self,data):

        new_node=DbNode(data)

        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
             new_node.next=self.head
             self.head.prev=new_node
             self.head=new_node
        self.size+=1

    def insert_at_end(self,data):
         new_node=DbNode(data)

         if self.head is None:
            self.head=new_node
            self.tail=new_node
         else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=self.tail.next
         self.size+=1

    def delete_at_first(self):

        if self.head is None:
            return False
        if self.head == self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
        self.size-=1

    def delete_at_last(self):
        if self.head is None:
            return False
        if self.head == self.tail:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
        self.size-=1
        


    def display_forward(self):
    
        current=self.head
        while current.next != None:
            print(current.data,end="->")
            current=current.next
        print(current.data)

    def display_reverse(self):
    
        current=self.tail
        while current.prev != None:
            print(current.data,end="->")
            current=current.prev
        print(current.data)

    def size_of_linkedlist(self):
        print(self.size);



db1=dbLinkedListWithHeadAndTail()
db1.insert_At_beg(10)
db1.insert_At_beg(20)
db1.insert_at_end(30)
# db1.delete_at_first()
db1.delete_at_last()
# db1.display_forward()
db1.display_reverse()
db1.size_of_linkedlist()
             
        