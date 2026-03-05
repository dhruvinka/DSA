# 1. Implement the following features for a circular singly linked list with only head/start
# pointer library.
# a. Create an Empty List
# b. Inserting Node
# i. as First Node,
# ii. as Last Node,
# iii. at desired location,
# c. Deleting Node
# i. at First,
# ii. at Last,
# iii. desired element,
# d. Display/ Traverse List
# e. Size of linked list

from Node import *;

class cirlinkedwithhead:
    
    def __init__(self) :
        self.head=None
        self.size=0
    
    def insert_at_beg(self,data):

        new_node=Node(data);
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            new_node.next=self.head
            curr=self.head
            while curr.next != self.head:
                 curr=curr.next
            self.head=new_node
            curr.next=new_node
        self.size+=1

    def insert_at_end(self,data):
        new_node=Node(data);
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            curr=self.head
            while curr.next != self.head:
                     curr=curr.next
            curr.next=new_node
            new_node.next=self.head
        self.size+=1

    def insert_at_pos(self,pos,data):
         
         new_node=Node(data)
         if pos < 0 or pos > self.size :
                return
         
         if pos == 0:
            self.insert_at_beg(data)
        
         if pos == self.size-1:
            self.insert_at_end(data)

         current=self.head
         pre=None
         for i in range(pos):
                pre=current
                current=current.next
            
         new_node.next=current
         pre.next=new_node
         self.size+=1
                

    
    def delete_at_first(self):
         if self.head is None:
                return
         if self.head.next == self.head:
                self.head =None
         else:
                # self.head=self.head.next
                curr=self.head
                while curr.next != self.head:
                     curr=curr.next
                self.head=self.head.next
                curr.next=self.head
         self.size-=1
        
    def delete_at_last(self):
         if self.head is None:
                return False
         if self.head.next == self.head:
                self.head =None
         else:
                curr=self.head
                prev=None
                while curr.next != self.head:
                     prev=curr
                     curr=curr.next
                prev.next=self.head
         self.size-=1

    def delete_at_pos(self,pos):
              
          if pos < 0 or pos > self.size:
                return False
          
          if pos == 0:
                self.delete_at_first()
                return  
          
          if pos == self.size:
                self.delete_at_last()
                return 

          current=self.head
          pre=None
          for i in range(pos):
                pre=current
                current=current.next
          pre.next=current.next
          self.size-=1

    def size_of_LinkedList(self):
         print(self.size)
                
         
                
    
    def display(self):
        if self.head is None:
            return "No Node"
        
        curr= self.head
        while curr.next != self.head:
                print(curr.data ,end= " -> ")
                curr=curr.next

        print(curr.data)
        curr=curr.next
        print("hii",curr.data)
        curr=curr.next
        # print("hii",curr.data)

    


s1=cirlinkedwithhead();
s1.insert_at_beg(20)
s1.insert_at_beg(30)
s1.insert_at_end(40)
s1.insert_at_end(50)
s1.insert_at_pos(1,100)
s1.display()
print("delete AT FIRST")
s1.delete_at_first()
s1.display()
print("delete AT FIRST")
s1.delete_at_last()
s1.display()
# s1.size_of_LinkedList()




        
        
