from LinkedList import *;
def reverse_linked_list(linked_list):
    if linked_list.head is None:
        print("Linked List is empty")
        return

    prev=None
    current=linked_list.head

    while current is not None:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node

    linked_list.head=prev


l1=LinkedList()
l1.insert_at_beg(10)
l1.insert_at_end(20)
l1.insert_at_end(30)
reverse_linked_list(l1)
l1.display()
