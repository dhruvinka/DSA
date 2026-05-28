
from Node import Node

class SingleLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def insert_at_value(self,data,value):
        new_node=Node(data)
        if self.head is None:
            print("List is empty. Inserting at the beginning.")
            return
        if self.head.data==value:
            self.insert_at_beginning(data)
            return
        curr=self.head
        found=False
        while curr is not None:
            if curr.data == value:
                found=True
                new_node.next=curr.next
                curr.next=new_node
                return
            curr=curr.next
        if not found:
            print(f"Value {value} not found in the list.")

    def insert_by_pos(self,data,pos):
        print("Index is start with 0 based")
        if self.head is None:
            return
        if pos < 0 or pos >= self.length():
            print("Invalid position")
            return
        if pos==0:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            curr = self.head
            for _ in range(pos - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()


if __name__ == "__main__":
    sll = SingleLL()
    arr = [64, 34, 25, 12, 22, 11, 90]
    for num in arr:
        sll.insert_at_end(num)
    
    print("Linked List:")
    sll.display()
    sll.insert_at_value(15, 22)
    sll.display()
