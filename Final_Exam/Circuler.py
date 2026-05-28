from Node import Node

class CircularLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next=self.head
            curr=self.head
            while curr.next != self.head:
                curr=curr.next
            curr.next=new_node
            self.head=new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next=self.head
            curr=self.head
            while curr.next != self.head:
                curr=curr.next
            curr.next=new_node
            new_node.next=self.head


    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        curr = self.head
        while True:
            print(curr.data, end=' ')
            curr = curr.next
            if curr == self.head:
                break
        print(curr.data)

if __name__ == "__main__":
    circular_list = CircularLL()
    circular_list.insert_at_beginning(10)
    circular_list.insert_at_beginning(20)
    circular_list.insert_at_beginning(30)
    circular_list.insert_at_end(40)

    print("Circular Linked List:")
    circular_list.display()