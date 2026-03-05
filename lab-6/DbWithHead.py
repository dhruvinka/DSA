from dbNode import Node

class DbWithHead:
    def __init__(self):
        self.head=None
        self.size=0

    def display(self):
            temp= self.head
            while temp is not None:
                print(temp.data, end= " -> ")
                temp= temp.next
            

    
    def insert_at_beg(self,data):

        new_node=Node(data)

        if self.head is None:
            self.head=new_node
        else:
            # first newnode.next assign to head then head.prev to newnode  final head to newnode
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.size+=1

    def insert_at_end(self,data):
         
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
        else:
            current = self.head
            while current.next is not None:
                current=current.next
            
            current.next=new_node
            new_node.prev=self.tail
            current=new_node

    def delete_at_beg(self):
        if self.head is None:
            return
        else:
            data = self.head.data
            if self.head.next is None:
                self.head=None
            else:
                self.head=self.head.next
                self.head.prev=None

            self.size-=1
            return data
        
    def delete_at_end(self):

        if self.head is None:
            return
        else:
            current = self.head
            while current.next is not None:
                current=current.next
            
            current=current.prev
            current.next=None
        
            self.size-=1
            



         


l1=DbWithHead()
l1.insert_at_beg(20)
l1.insert_at_beg(30)
# l1.display()
# print()
# l1.delete_at_beg()
l1.delete_at_end()
l1.display()
