from Node import *;

class LinkedList:

    def __init__(self):
        self.head= None
        self.size= 0

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current=self.head
            
            while current.next is not self.head:
                print(current.data, end= "->")
                current= current.next
            print(current.data, end= "->")



    def insert_at_beg(self,data):

        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            new_node.next=self.head  # circuler new node point it self
            self.size+=1
        else:
            new_node.next=self.head
            
            current=self.head
            while current.next is not self.head:
                current=current.next
            
            self.head=new_node 
            current.next=self.head
            self.size+=1



    def insert_at_end(self,data):
        
        new_node=Node(data)

        if self.head is None:
            new_node.next=self.head
            new_node.next=self.head

            self.size+=1
            return
        current=self.head
         
        # go to the last node
        while current.next is not self.head:
            current=current.next

        current.next=new_node
        
        # at last node point to first
        new_node.next=self.head
        self.size+=1
    
    def insert_at_Between(self,data,position):

        if position < 0 or position > self.size :
            return False   
             
        if position==0:
            self.insert_at_beg(data)

        if position==self.size:
            self.insert_at_end(data)

        new_node=Node(data)

        current=self.head
        pre=None

        for i in range(position):
            pre=current
            current=current.next
        
        new_node.next=current
        pre.next=new_node
        self.size+=1

    
    def delete_at_first(self):
        if self.head is None:
            print("Linked List is empty")
        
        self.head=self.head.next
        self.size-=1

    def delete_at_last(self):
         if self.head is None:
            print("Linked List is empty")
        
         current=self.head
         pre=None

        # goes to last node
         while current.next is not self.head:
             pre=current
             current=current.next
        
        # at last node point to first
         pre.next=self.head
         self.size-=1

    def deletea_at_Between(self,position):
        # zero index base start

        if position < 0 or position > self.size:
            return False
        
        if position == 0:
            self.delete_at_first()
            return

        if position == self.size-1:
            self.delete_at_last()
            return

        current = self.head
        prev=None
        for i in range(position-1):
            prev=current
            print("prev",prev.data)
            current=current.next
            print("current",current.data)
        
        print("final prev",prev.data)
        print("final current",current.data)
        prev.next=current.next
        self.size-=1




l1=LinkedList()
l1.insert_at_beg(10)
l1.insert_at_beg(20)
l1.insert_at_beg(30)
l1.insert_at_end(11)
# l1.insert_at_end(13)
# l1.insert_at_Between(12,1)
l1.display()
# l1.delete_at_first()
# l1.delete_at_last()
# l1.deletea_at_Between(1)
# l1.insert_at_beg(30)
# l1.display()





    
