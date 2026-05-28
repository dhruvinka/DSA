from DbNode import DbNode

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def insert_at_beg(self,data):
        new_node=DbNode(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.size+=1
    

    def insert_at_end(self,data):
        new_node=DbNode(data)
        if self.head is None:
            self.head=new_node
        else:
            pre=self.head
            while pre.next is not None:
                pre=pre.next
            pre.next=new_node
            new_node.prev=pre
        self.size+=1

    def delete_at_beg(self):
        if self.head is None:
            print("Empty")
            return
        self.head=self.head.next
        self.head.prev=None
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
            prev=None
            while curr.next is not None:
                prev=curr
                curr=curr.next
            prev.next=None
            self.size-=1
            
            
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print()
    
    def reverse(self):
        current=self.head
        new_head=None
        while current is not None:
            current.prev, current.next = current.next, current.prev
            new_head=current
            current=current.prev  # move forward (prev is now old next after swap)
        self.head=new_head


if __name__ == "__main__":
    s=DoublyLinkedList()
    s.insert_at_beg(1)
    s.insert_at_beg(2)
    s.insert_at_end(4)
    s.insert_at_beg(3)
    s.insert_at_end(5)
    s.display()
    s.delete_at_end()
    s.display()
    s.delete_at_beg()
    s.display()

   

        

    
