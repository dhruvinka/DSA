from DbNode import Node

class DbWithHead:
    def __init__(self):
        self.head=None
        self.size=0
    
    def insert_at_beg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.size+=1

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next != None:
                curr=curr.next
            
            new_node.prev=curr
            curr.next=new_node
        self.size+=1

    def insert_at_pos(self,pos,data):
        if pos < 0 or pos > self.size:
            return False
        
        if pos == 0:
            self.insert_at_beg(data)
            return
        elif pos == self.size  :
            print("pos",pos)
            self.insert_at_end(data)
            return
        else:
            new_node=Node(data)
            curr=self.head

            for i in range(pos):
                curr=curr.next

            new_node.prev=curr.prev
            curr.prev.next=new_node
            new_node.next=curr
         
        self.size +=1



    def delete_at_beg(self):
           
           if self.head is None:
                  return False
           if self.head.next is None:
               self.head=None
           else:
               self.head=self.head.next
               self.head.prev=None
           self.size-=1

    def delete_at_end(self):
           if self.head is None:
                  return False
           if self.head.next is None:
               self.head=None
           else:
               curr=self.head
               while curr.next != None:
                   curr=curr.next
                
               data=curr.data
               curr.prev.next=None
               curr.prev=None

           self.size-=1
           return data
    
    def delete_at_pos(self,pos):

         # indexing starts from 0 to size-1
         
        if pos < 0 or pos >= self.size:
            return False
        
        if pos == 0:
            self.delete_at_beg()
            return
        elif pos == self.size - 1 :
            self.delete_at_end()
        else:
            curr=self.head

            for i in range(pos):
                curr=curr.next
            curr.prev.next=curr.next
            curr.next.prev=curr.prev
        self.size -=1
        



    def dis(self):
        if self.head is None:
            return False
        else:
            curr=self.head

            while curr.next != None:
                print(curr.data ,end= " -> ")
                curr=curr.next
            print(curr.data)

    def dis_rev(self):
        if self.head is None:
            return False
        else:
            curr=self.head

            while curr.next != None:
                curr=curr.next

            while curr.prev != None:
                print(curr.data ,end= " -> ")
                curr=curr.prev
            print(curr.data)


        



l1=DbWithHead()
l1.insert_at_beg(10)
l1.insert_at_beg(20)
l1.insert_at_end(30)
l1.insert_at_pos(0,50)
l1.insert_at_pos(4,60)
# l1.delete_at_beg()
l1.dis()
# print("Deleted Value",l1.delete_at_end())
print(l1.size)
# print("Deleted Value",l1.delete_at_pos(2))
l1.dis()
# l1.dis_rev()