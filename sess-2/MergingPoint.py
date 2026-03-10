from SingleLinkedListWithHeadtail import *

class Node:
    def __init__(self):
        self.l1 = SingleLinkedList()
        self.l2 = SingleLinkedList()

    def find_merging_point_with_stack(self):
        head1 = self.l1.head
        head2 = self.l2.head
        
        # FIXED CONDITION
        if not head1 or not head2:
            return None
        
        stack1 = []
        stack2 = []
        
        current = head1
        while current:
            stack1.append(current)
            current = current.next
        
        current = head2
        while current:
            stack2.append(current)
            current = current.next
        
        merging_point = None
        
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            
            if node1 == node2:
                merging_point = node1
            else:
                break
        
        return merging_point

# Create intersection by sharing nodes
x = Node()

# Create a node that will be shared (intersection point)
from Node import Node as ListNode  # Import your Node class
intersection_node = ListNode(99)

# Build first list: 2 -> 1 -> 3 -> 99 -> 100
x.l1.insert_At_beg(1)
x.l1.insert_At_beg(2)
x.l1.insert_At_end(3)

# Manually add intersection node
current = x.l1.head
while current.next:
    current = current.next
current.next = intersection_node
x.l1.tail = intersection_node

# Add node after intersection
after_intersection = ListNode(100)
intersection_node.next = after_intersection
x.l1.tail = after_intersection

# Build second list: 3 -> 4 -> 1 -> 99 -> 100
x.l2.insert_At_beg(4)
x.l2.insert_At_beg(3)
x.l2.insert_At_end(1)

# Connect to same intersection node
current = x.l2.head
while current.next:
    current = current.next
current.next = intersection_node
x.l2.tail = after_intersection

# Display lists
print("List 1:")
x.l1.dis()
print("\nList 2:")
x.l2.dis()

# Find merging point
result = x.find_merging_point_with_stack()
if result:
    print(f"\n✓ Merging point found at node with value: {result.data}")
else:
    print("\n✗ No merging point found")