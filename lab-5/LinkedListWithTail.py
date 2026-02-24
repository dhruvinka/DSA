from Node import *;

# only need to change in add_in_first,last and delete_first,last
class LinkedList:

    def __init__(self):
        self.head= None
        self.tail=None
        self.size= 0

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp= self.head
            while temp is not None:
                print(temp.data, end= "->")
                temp= temp.next
            print()

    def insert_at_beg(self,data):
       
        if self.head is None:
              new_node=Node(data)
              new_node.next=self.head
              self.head=new_node
              self.tail=new_node
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
            self.size+=1

    def insert_at_end(self,data):
         
         # if linked list is empty then head=new and tail=new
         # if already element in it then tail.next=new and then switch tail=new 

        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
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

        #if head become none after delete at means no element so need to None also tail
        if self.head is None:
            self.tail=None

    def delete_at_last(self):
         if self.head is None:
            print("Linked List is empty")
        
         current=self.head
        
        # goes up to current.next == tail  so it give the second last node
         while current.next != self.tail:
             current=current.next

         #second last node we assign tail and next to None 
         current.next=None
         self.tail=current
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
l1.insert_at_end(11)
l1.insert_at_end(13)
l1.insert_at_Between(12,1)
l1.display()
l1.delete_at_last()
l1.display()





    
