from Node import Node;

class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    
    def insert_At_beg(self,data):

        if self.head is None:
            new_Node=Node(data)
            self.head=new_Node
            new_Node.next=None
        else:
            new_Node=Node(data)
            new_Node.next=self.head
            self.head=new_Node
        self.size +=1

    def insert_At_end(self,data):
        if self.head is None:
            new_Node=Node(data)
            self.head=new_Node
            new_Node.next=None
        else:
            curr=self.head
            while curr.next != None:
                curr=curr.next
            
            new_Node=Node(data)
            curr.next=new_Node
        self.size+=1

    def insert_at_pos(self,pos,data):
         
        if pos < 0 or pos > self.size:
            return False
        
        if pos == 0:
            self.insert_At_beg(data)
        elif pos == self.size :
            self.insert_At_end(data)
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
        else:
            self.head=self.head.next
            self.size-=1
    
    def delete_at_end(self):
        if self.head is None:
            return False
        if self.head.next is None:
            self.head=None
            self.size-=1
        else:
            curr=self.head
            prev=None

            while curr.next != None:
                prev=curr
                curr=curr.next

            prev.next=None
            self.size-=1


    def delete_at_pos(self,pos):

        # indexing starts from 0 to size-1
         
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
            
            print("prev.data",prev.data)
            print("curr.data",curr.data)
            prev.next=curr.next
            self.size-=1

    def middle(self):
        if self.head is None:
            return
        slow=self.head
        fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow.data

        
    def dis(self):
        if self.head is None:
            return False
        
        curr=self.head
        while curr.next != None:
            print(curr.data ,end=' -> ')
            curr=curr.next
        print(curr.data)


l1=SingleLinkedList()
l1.insert_At_beg(10)
l1.insert_At_beg(20)
l1.insert_At_end(30)
l1.insert_at_pos(2,40)
l1.insert_at_pos(2,50)
# l1.delete_at_beg()
# l1.delete_at_end()
l1.dis()
# l1.delete_at_pos(2)
print(l1.middle())
l1.dis()
    
