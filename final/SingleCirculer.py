from Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            new_node.next=self.head
            curr=self.head
            while curr.next is not self.head:
                curr=curr.next
            curr.next=new_node
            self.head=new_node
        self.size+=1

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not self.head:
                curr=curr.next
            new_node.next=curr.next
            curr.next=new_node
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
            curr=self.head
            for i in range(pos-1):
                curr=curr.next
            new_node.next=curr.next
            curr.next=new_node
        self.size+=1

    def insert_after_value(self,data,val):
        new_node=Node(data)
        curr=self.head
        while curr is not None:
            if curr.data == val:
                new_node.next=curr.next
                curr.next=new_node
                self.size+=1
                return
            curr=curr.next
        print("Value not found")


    def delete_at_beg(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head=None
        else:
            curr=self.head
            prev=None
            while curr.next is not self.head:
                prev=curr
                curr=curr.next
            curr.next=self.head.next
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
            curr=self.head
            pre=None
            while curr.next is not self.head:
                pre=curr
                curr=curr.next
            pre.next=curr.next
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
            curr=self.head
            for i in range(pos-1):
                curr=curr.next
            curr.next=curr.next.next
            self.size-=1

    def delete_by_value(self,val):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == val:
            self.head=self.head.next
            self.size-=1
            return
        curr=self.head
        while curr.next is not None:
            if curr.next.data == val:
                curr.next=curr.next.next
                self.size-=1
                return
            curr=curr.next
        print("Value not found")

        

    def display(self):
        temp=self.head
        while temp.next is not self.head:
            print(temp.data,end="->")
            temp=temp.next
        print(temp.data)
        # temp=temp.next
        # print(temp.data)
        print()

s=SinglyLinkedList()
s.insert_at_beg(1)
s.insert_at_beg(2)
s.insert_at_end(4)
s.insert_at_beg(3)
s.insert_at_end(5)
# s.insert_at_pos(6,5)
# s.insert_after_value(7,4)
s.display()
s.delete_at_beg()
s.display()
s.delete_at_end()
s.display()
# s.delete_at_pos(2)
# s.display()
# s.delete_by_value(7)


# s.display()