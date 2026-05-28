from DbNode import Node

class dbLL:
    def __init__(self):
        self.head=None
        

    def insert_at_beg(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def insert_at_end(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            new_node=Node(data)
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            new_node.prev=curr
            curr.next=new_node
            new_node.next=None

    def deletefirst(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None
        
    def deletelast(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head=None
        else:
            curr=self.head
            while curr.next.next is not None:
                curr=curr.next
            curr.next=None
            
        
    def dis(self):
        curr=self.head
        while curr.next is not None:
            print(curr.data,end=" ")
            curr=curr.next
        print(curr.data)

ls=dbLL()
ls.insert_at_beg(10)
ls.insert_at_beg(20)
ls.insert_at_beg(110)
ls.insert_at_end(50)
ls.insert_at_end(70)
ls.deletefirst()
ls.deletefirst()
ls.deletelast()
ls.dis()




