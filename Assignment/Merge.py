from LinkedList import *
import sys

class Merge:
    def __init__(self):
        self.l1 = LinkedList()
        self.l2 = LinkedList()
        self.l3 = LinkedList()

    def sortLinkedList(self, head):
        curr = head

        while curr is not None:
            runner = curr.next

            while runner is not None:
                if curr.data > runner.data:
                    curr.data, runner.data = runner.data, curr.data
                runner = runner.next

            curr = curr.next
        return head

    def merge(self, head1, head2):
        self.l3 = LinkedList()  

        while head1 and head2:
            if head1.data < head2.data:
                self.l3.insert_at_end(head1.data)
                head1 = head1.next
            else:
                self.l3.insert_at_end(head2.data)
                head2 = head2.next

        while head1:
            self.l3.insert_at_end(head1.data)
            head1 = head1.next

        while head2:
            self.l3.insert_at_end(head2.data)
            head2 = head2.next

        return self.l3.head

    def display(self, head):
        curr = head
        while curr is not None:
            print(curr.data, end=" → ")
            curr = curr.next
        print("None")

Ll = Merge()

li = len(sys.argv)
print(li)

for i in range(1,li//2+1):
    Ll.l1.insert_at_end(int(sys.argv[i]))

for i in range(li//2+1, li):
    Ll.l2.insert_at_end(int(sys.argv[i]))

Ll.l1.display()
Ll.l2.display()

# sort both
head1=Ll.sortLinkedList(Ll.l1.head)
head2=Ll.sortLinkedList(Ll.l2.head)

print("L1 after sorting:")
Ll.l1.display()

print("L2 after sorting:")
Ll.l2.display()

print("Merged List:")
M=Ll.merge(head1,head2)
Ll.display(M)