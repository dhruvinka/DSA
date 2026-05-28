from DbNode import DbNode

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def insert_at_beg(self,data):
        new_node=DbNode(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node

        else:
            curr=self.head
            while curr.next is not self.head:
                curr=curr.next
            
            new_node.next=self.head
            new_node.prev=curr
            curr.next=new_node
            self.head.prev=new_node
            self.head=new_node

            # new_node.next=self.head
            # self.head.prev=curr
            # self.head=new_node
            # curr.next=self.head
        
        self.size+=1
    

    def insert_at_end(self,data):
        new_node=DbNode(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            curr=self.head
            while curr.next is not self.head:
                curr=curr.next
            new_node.prev=curr
            new_node.next=curr.next
            curr.next=new_node
            self.head.prev=new_node

        self.size+=1

    def delete_at_beg(self):
        if self.head is None:
            print("Empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
           curr=self.head
           while curr.next is not self.head:
               curr=curr.next
           curr.next=self.head.next
           self.head.next.prev=curr
           self.head=self.head.next
        self.size -= 1

    def delete_at_end(self):
        if self.head is None:
            print("Empty")
            return
        if self.head.next == self.head:  
            self.head = None
        else:
           curr=self.head
           pre=None
           while curr.next is not self.head:
               pre=curr
               curr=curr.next
           pre.next=curr.next
           self.head.prev=pre
    
        self.size -= 1
            
            
    def display(self):
        if self.head is None:
            print("Empty list")
            return
        
        curr=self.head

        while curr.next is not self.head:   
            print(curr.data,end="->")
            curr=curr.next
        print(curr.data)
        # curr=curr.next
        # print(curr.data)
        print()
    


if __name__ == "__main__":
    s=DoublyLinkedList()
    s.insert_at_beg(1)
    s.insert_at_beg(2)
    s.insert_at_end(4)
    s.insert_at_beg(3)
    s.insert_at_end(5)
    s.insert_at_end(7)
    s.display()
    s.delete_at_end()
    # s.display()
    s.delete_at_beg()
    s.display()

   

        

    
