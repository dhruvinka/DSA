from Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.size+=1

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            tmp=self.head
            while tmp.next is not None:
                tmp=tmp.next
            tmp.next=new_node
        self.size+=1


    def insert_at_pos(self,data,pos):
        if pos<0 or pos>self.size:
            print("Invalid position")
            return
        new_node=Node(data)
        if pos==0:
            self.insert_at_beg(data)
        elif pos==self.size:
            self.insert_at_end(data)
        else:
            tmp=self.head
            for i in range(pos-1):
                tmp=tmp.next
            new_node.next=tmp.next
            tmp.next=new_node
        self.size+=1

    def insert_after_value(self,data,val):
        new_node=Node(data)
        tmp=self.head
        while tmp is not None:
            if tmp.data == val:
                new_node.next=tmp.next
                tmp.next=new_node
                self.size+=1
                return
            tmp=tmp.next
        print("Value not found")


    def delete_at_beg(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next
        self.size-=1

    def delete_at_end(self):
        if self.head is None:
            print("Empty")
            return
        if self.head.next is None:
            self.head=None
            self.size-=1
        else:
            tmp=self.head
            while tmp.next.next is not None:
                tmp=tmp.next
            tmp.next=None
            self.size-=1

    def delete_at_pos(self,pos):
        if pos<0 or pos>=self.size:
            print("Invalid position")
            return
        if pos==0:
            self.delete_at_beg()
        elif pos==self.size-1:
            self.delete_at_end()
        else:
            tmp=self.head
            for i in range(pos-1):
                tmp=tmp.next
            tmp.next=tmp.next.next
            self.size-=1

    def delete_by_value(self,val):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == val:
            self.head=self.head.next
            self.size-=1
            return
        tmp=self.head
        while tmp.next is not None:
            if tmp.next.data == val:
                tmp.next=tmp.next.next
                self.size-=1
                return
            tmp=tmp.next
        print("Value not found")

        

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print()

s=SinglyLinkedList()
s.insert_at_beg(1)
s.insert_at_beg(2)
s.insert_at_end(4)
s.insert_at_beg(3)
s.insert_at_end(5)
s.insert_at_pos(6,5)
# s.insert_after_value(7,4)


s.display()