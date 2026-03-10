from Node import Node

class CirculerLinklistWithHeadTail:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insert_at_beg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
        self.size+=1
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=self.head
        else:
            self.tail.next=new_node
            self.tail=new_node
            new_node.next=self.head
        self.size+=1

    def insert_at_pos(self,pos,data):
        if pos < 0 or pos > self.size:
            return False
        
        if pos == 0:
            self.insert_at_beg(data)
        elif pos == self.size :
            self.insert_at_end(data)
        else :
            curr=self.head
            prev=None
            for i in range(pos):
                prev=curr
                curr=curr.next
            
            new_node=Node(data)
            new_node.next=curr
            prev.next=new_node
            self.size+=1

    def delete_at_beg(self):
        if self.head is None:
            return False
        if self.head.next is None:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
        self.size-=1

    def delete_at_end(self):
        if self.head is None:
            return False
        if self.head.next is None:
            self.head=None
            self.tail=None
        else:
            curr=self.head
            prev=None
            while curr.next != self.head:
                prev=curr
                curr=curr.next
            
            prev.next=self.head
            self.tail=prev
        self.size-=1
    
    def delete_at_pos(self,pos):
        if pos < 0 or pos >= self.size:
            return False
        
        if pos == 0:
            self.delete_at_beg()
        elif pos == self.size -1 :
            self.delete_at_end()
        else :
            curr=self.head
            prev=None
            for i in range(pos):
                prev=curr
                curr=curr.next
            
            prev.next=curr.next
            curr.next=None
            self.size-=1

    def display(self):
        if self.head is None:
            print("List is empty")
        
        else:
            curr= self.head

            while curr.next != self.head:
                print(curr.data, end= " -> ")
                curr=curr.next
            print(curr.data)
            curr=curr.next
            print(curr.data)


    def is_loop(self):
        if self.head is None:
            print("Linked List is Empty")
        
        slow=self.head
        fast=self.head

        while fast !=None and fast.next != None:
            slow=slow.next
            fast=fast.next.next

            if slow == fast:
                return True
            
        return False
        

l1=CirculerLinklistWithHeadTail()
l1.insert_at_beg(10)
l1.insert_at_beg(20)
l1.insert_at_end(30)
l1.insert_at_pos(1, 25)
# l1.delete_at_beg()
# l1.delete_at_end()
print(l1.is_loop())
l1.display()