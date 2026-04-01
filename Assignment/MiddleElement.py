from LinkedList import *;
import sys

def middle_element(linked_list):
    if linked_list.head is None:
        print("Linked List is empty")
        return

    current = linked_list.head
    prev=None
     #first Way
    print(linked_list.size)
    for i in range(linked_list.size//2):
        prev=current
        current=current.next
    print("Middle element is ",current.data)

    # sl=linked_list.head
    # fast=linked_list.head

    # while fast and fast.next:
    #     sl=sl.next
    #     fast=fast.next.next
    


l1=LinkedList()

li = len(sys.argv)
print(li)

for i in range(1,li):
    print(sys.argv[i])
    l1.insert_at_beg(int(sys.argv[i]))
# l1.insert_at_beg(10)
# l1.insert_at_end(11)
# l1.insert_at_end(14)
# l1.insert_at_Between(12,1)
# l1.insert_at_Between(13,1)
l1.display()
middle_element(l1)
