from Node import Node

class CirculerLinklistWithTail:
    # using only tail pointer
    def __init__(self):
        self.tail=None
        self.size=0
    
    def insert_at_beg(self,data):
        new_node=Node(data)
        if self.tail is None:
            self.tail=new_node
            new_node.next=self.tail
        else:
            new_node.next=self.tail.next
            self.tail.next=new_node
        self.size+=1
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.tail is None:
            self.tail=new_node
            new_node.next=self.tail
        else:
            new_node.next=self.tail.next
            self.tail.next=new_node
            self.tail=new_node
        self.size+=1

    def insert_at_pos(self,pos,data):
        if pos < 0 or pos > self.size:
            return False
        
        if pos == 0:
            self.insert_at_beg(data)
        elif pos == self.size :
            self.insert_at_end(data)
        else :
            curr=self.tail.next
            prev=None
            for i in range(pos):
                prev=curr
                curr=curr.next
            
            new_node=Node(data)
            new_node.next=curr
            prev.next=new_node
            self.size+=1
    
    def delete_at_beg(self):
        if self.tail is None:
            return False
        if self.tail.next is None:
            self.tail=None
        else:
            self.tail.next=self.tail.next.next
        self.size-=1
    
    def delete_at_end(self):
        if self.tail is None:
            return False
        if self.tail.next is None:
            self.tail=None
        else:
            curr=self.tail.next
            prev=None
            while curr.next != self.tail.next:
                prev=curr
                curr=curr.next
            
            prev.next=self.tail.next
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
            curr=self.tail.next
            prev=None
            for i in range(pos):
                prev=curr
                curr=curr.next
            
            prev.next=curr.next
            self.size-=1

    def display(self):
        if self.tail is None:
            print("List is empty")
            return
        
        curr=self.tail.next
        while curr is not None:
            print(curr.data,end=" -> ")
            curr=curr.next
            if curr == self.tail.next:
                break
        print()

l1=CirculerLinklistWithTail()
l1.insert_at_beg(100)
l1.insert_at_end(10)
l1.insert_at_end(20)
l1.insert_at_end(30)
l1.display()
l1.insert_at_pos(1, 25)
l1.display()
l1.delete_at_pos(1)
l1.display()
q1=l1.delete_at_end()
print("Deleted data is ",q1)
l1.display()
