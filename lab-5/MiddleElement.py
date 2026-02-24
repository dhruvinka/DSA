from LinkedList import *;

def middle_element(linked_list):
    if linked_list.head is None:
        print("Linked List is empty")
        return

    current = linked_list.head
    prev=None

    for i in range(linked_list.size//2):
        prev=current
        current=current.next
    print("Middle element is ",current.data)
    


l1=LinkedList()
l1.insert_at_beg(10)
l1.insert_at_end(11)
l1.insert_at_end(14)
l1.insert_at_Between(12,1)
l1.insert_at_Between(13,1)
l1.display()
middle_element(l1)
