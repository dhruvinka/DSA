from LinkedList import *

class ispalindeom:
    def __init__(self):
        self.l1 = LinkedList()
        self.l2 = LinkedList()

    def palindrome(self):
        if self.l1.head is None:
            return True
        
        slow = self.l1.head
        fast = self.l1.head
        count = 0
        
        while fast and fast.next:
            count += 1
            slow = slow.next
            fast = fast.next.next
        
        tmp = slow
        while tmp.next != None:
            self.l2.insert_at_beg(tmp.data)  
            tmp = tmp.next
        self.l2.insert_at_beg(tmp.data)  
       
        curr1 = self.l1.head
        curr2 = self.l2.head
        
       
        for i in range(count):
            if curr1.data != curr2.data:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        
        return True

x = ispalindeom()

x.l1.insert_at_beg(1)
x.l1.insert_at_end(2)
x.l1.insert_at_end(3)
x.l1.insert_at_end(2)
x.l1.insert_at_end(1)
x.l1.display()
print("Is palindrome?", x.palindrome())
x.l2.display()



x2 = ispalindeom()
x2.l1.insert_at_beg(1)
x2.l1.insert_at_end(2)
x2.l1.insert_at_end(3)
x2.l1.insert_at_end(4)
x2.l1.insert_at_end(5)
x2.l1.display()
print("Is palindrome?", x2.palindrome())